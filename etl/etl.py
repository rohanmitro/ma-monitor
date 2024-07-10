import os
import re
import pandas as pd
import spacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Load the German NLP model
nlp = spacy.load('de_core_news_sm')

# Download NLTK stopwords if not already downloaded
import nltk
nltk.download('stopwords')

# Function to preprocess the text data
def preprocess_text(text):
    text = re.sub(r'\n', ' ', text)  # Remove newline characters
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    text = re.sub(r'[^\w\s,]', '', text)  # Remove non-word characters but keep commas
    text = text.lower()  # Convert to lowercase
    tokens = word_tokenize(text)  # Tokenize the text
    tokens = [word for word in tokens if word not in stopwords.words('german')]  # Remove German stopwords
    return ' '.join(tokens)

# Function to extract entities
def extract_entities(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

# Function to extract acquirer, acquired entity, price, and price unit
def extract_acquisition_info(text, entities):
    acquirer = None
    acquired_entity = None
    price = None
    price_unit = None
    acquirer_pattern_used = None
    acquired_pattern_used = None
    price_pattern_used = None
    
    # Define patterns for extraction
    acquirer_patterns = [
        r'(?:übernahme durch|akquisition durch|fusion mit|erworben von|aufgekauft von|verkaufen|veräußern|übernehmen|fusionieren|übernommen von|kauften|erwarben|akquirierten|kauf|erwerb durch)\s+([\w\s,]+)',
        r'([\w\s,]+)\s+(?:erwirbt|kauft|übernimmt|fusioniert mit|akquiriert)'
    ]

    acquired_patterns = [
        r'(?:übernimmt|akquiriert|fusioniert mit|erwirbt)\s+([\w\s,]+)',
        r'(?:anbieter von|anbieter|unternehmen|firmen|konzerne|betriebe)\s+([\w\s,]+)',
        r'([\w\s,]+)\s+(?:wird übernommen von|wurde übernommen von|wird fusioniert mit|fusioniert mit|akquiriert von|gekauft von|übernommen von)'
    ]
    price_patterns = [
        r'(\d+[\.,]?\d*)\s?(millionen|milliarden)?\s?(euro|usd|usdollar|dollar)?'
    ]

    # Find acquirer
    for pattern in acquirer_patterns:
        acquirer_match = re.search(pattern, text)
        if acquirer_match:
            acquirer = acquirer_match.group(1).strip()
            acquirer_pattern_used = pattern
            break

    # Find acquired entity
    for pattern in acquired_patterns:
        acquired_match = re.search(pattern, text)
        if acquired_match:
            acquired_entity = acquired_match.group(1).strip()
            acquired_pattern_used = pattern
            break

    # Find price and price unit
    for pattern in price_patterns:
        price_match = re.search(pattern, text)
        if price_match:
            price = price_match.group(1)
            price_unit = ' '.join(filter(None, [price_match.group(2), price_match.group(3)])).strip()
            price_pattern_used = pattern
            break
    
    # Verify acquirer and acquired entity with entities
    acquirer_entities = [entity for entity, label in entities if label == 'ORG' and entity.lower() in acquirer.lower()] if acquirer else []
    acquired_entities = [entity for entity, label in entities if label == 'ORG' and entity.lower() in acquired_entity.lower()] if acquired_entity else []
    other_entities = [entity for entity, label in entities if entity not in acquirer_entities and entity not in acquired_entities and label == 'ORG']
    
    
    return acquirer, acquired_entity, price, price_unit, acquirer_pattern_used, acquired_pattern_used, price_pattern_used, acquirer_entities, acquired_entities, other_entities

# Directory containing the data files
data_dir = 'data'

# Read all CSV files in the data directory
all_files = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.endswith('.csv')]
df_list = [pd.read_csv(file) for file in all_files]

# Concatenate all dataframes
df = pd.concat(df_list, ignore_index=True)
df = df.dropna(subset=['description'])  # Drop rows with missing descriptions

# Clean and preprocess the text data
df['cleaned_text'] = df['description'].apply(preprocess_text)
# Extract entities for each description
df['description_entities'] = df['description'].apply(extract_entities)

# Extract acquirer, acquired entity, price, and price unit information
df[['acquirer', 'acquired_entity', 'price', 'price_unit', 'acquirer_pattern', 'acquired_pattern', 'price_pattern', 'acquirer_entities', 'acquired_entities', 'named_entities']] = df.apply(
    lambda row: pd.Series(extract_acquisition_info(row['cleaned_text'], row['description_entities'])), axis=1)

# Keep only relevant columns
df_result = df[['title', 'description', 'acquirer', 'acquired_entity', 'price', 'price_unit', 'url', 'acquirer_entities', 'acquired_entities', 'named_entities']]
# Remove rows with missing acquirer or acquired entity
# df_result = df_result.dropna(subset=['acquirer', 'acquired_entity'])

# Remove prices which does not have a unit - they are potentially incorrect, e.g have years, etc. can be '' or None
df_result = df_result[df_result['price_unit'].notnull() & (df_result['price_unit'] != '')]
# Save to CSV
output_file = os.path.join('output/newsapi', 'acquisitions.csv')
df_result.to_csv(output_file, index=False)

# Display the result for verification
print(df_result.head())
