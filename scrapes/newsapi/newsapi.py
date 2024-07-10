import os
import requests
import pandas as pd
from datetime import datetime, timedelta

# Function to fetch news articles from NewsAPI
def fetch_news(api_key, query, from_date, to_date, language='de', page_size=100):
    url = ('https://newsapi.org/v2/everything?'
           'q={query}&'
           'from={from_date}&'
           'to={to_date}&'
           'language={language}&'
           'pageSize={page_size}&'
           'apiKey={api_key}')
    
    response = requests.get(url.format(query=query, from_date=from_date, to_date=to_date, language=language, page_size=page_size, api_key=api_key))
    articles = response.json().get('articles', [])
    return articles

# Parameters
api_key = os.getenv('NEWS_API_KEY')  # Fetch API key from environment variable
if not api_key:
    raise ValueError("No API key found. Please set the NEWS_API_KEY environment variable.")

search_phrases = [
    'Fusionen und Übernahmen',  # Mergers and acquisitions
    'Unternehmensübernahme',    # Company takeover
    'Fusion',                   # Merger
    'Akquisition',              # Acquisition
    'Übernahme'                 # Takeover
]
# Lowercase the search phrases
search_phrases = [phrase.lower() for phrase in search_phrases]
from_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
to_date = datetime.now().strftime('%Y-%m-%d')
language = 'de'

# Fetch news articles for each search phrase
all_articles = []
for phrase in search_phrases:
    articles = fetch_news(api_key, phrase, from_date, to_date, language)
    all_articles.extend(articles)

# Convert to DataFrame
df = pd.DataFrame(all_articles)

# Save to CSV
df.to_csv(f'data/german_ma_articles_{from_date}_{to_date}.csv', index=False)
