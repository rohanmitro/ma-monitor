# ma-monitor
# Mergers & Acquisitions Monitor PoC

## Overview

This project is a Proof of Concept (PoC) for monitoring and extracting information on mergers and acquisitions (M&A) in Germany. The project leverages various data sources and text parsing techniques to extract relevant M&A information from news articles.

```bash
├── data               # Raw data files (Input)
├── output             
│   ├── newsapi        # Output for NewsAPI scraping
├── notebooks          # Any Jupyter notebooks for analysis and development(Future)
├── scrapes            # Scripts for data scraping
│   ├── newsapi        # Scripts for NewsAPI scraping
├── etl                # ETL (Extract, Transform, Load) scripts
├── reports            # Generated reports and summaries (Future)
├── requirements.txt   # Python dependencies
└── README.md          # Project README
```
## Project Goals

- **Automate Data Collection**: Use web scraping, APIs, and RSS feeds to gather M&A information from various sources.
- **Data Processing**: Apply Natural Language Processing (NLP) and regular expressions to extract specific details from the collected data.
- **Data Storage**: Store the processed data in a structured format for easy querying and analysis.
- **Data Analysis and Visualization**: Generate reports and dashboards to visualize M&A trends and activities.

## Data Sources
### Used in PoC
- [News API](https://newsapi.org): Aggregates news articles from various sources. Used to fetch German-language articles related to M&A.
### Sample Output

| Title                                                                                                 | Description                                                                                                                                           | Named Entities                                    | Price | Price Unit      |
|-------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|-------|-----------------|
| Großübernahme: Milliardendeal um Aareon                                                               | Die Aareal Bank und der Finanzinvestor Advent verkaufen den Anbieter von Immobiliensoftware Aareon. Die IT-Gesellschaft wird mit 3,9 Milliarden Euro bewertet. Besonders interessant ist ein sonst selten genanntes Detail: die Höhe der Transaktionskosten. | ['Aareal Bank', 'IT-Gesellschaft']                | 3,9   | Milliarden Euro |
| Zurich bedient sich bei AIG                                                                           | Die Zurich-Gruppe kauft das Reiseversicherungs- und Assistancegeschäft des New Yorker Versicherers. Der Bereich firmiert bislang unter der Marke AIG Travel. Die Schweizer legen für die Sparte, die derzeit auch bei der Allianz hoch im Kurs steht, 600 Millionen… | ['Zurich-Gruppe', 'AIG Travel', 'Allianz']        | 600   | Millionen       |
| Boeing kauft Zulieferer Spirit zurück                                                                 | Für knapp 4,7 Milliarden Dollar kauft Boeing den wichtigen US-Zulieferer Spirit Aerosystems. Für den Flugzeughersteller ist die Übernahme der ehemaligen Konzernsparte ein wichtiger Schritt zur Qualitätssicherung. | ['Boeing', 'US-Zulieferer', 'Spirit Aerosystems'] | 4,7   | Milliarden Dollar |

### Potential Data Sources
| **Category**               | **Source**                                           | **Type**             | **Description**                                                                 | **URL**                                                             | **RSS Feed**                                                        |
|----------------------------|------------------------------------------------------|----------------------|---------------------------------------------------------------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------|
| **News Aggregators**       | Google News                                          | Web Scraping     | Comprehensive source for various news articles, including press releases and financial news. | [Google News](https://news.google.com)                              | No                                                                  |
|                            | Bing News                                            | API/Web Scraping     | General news aggregator for cross-referencing and verification.                | [Bing News](https://www.bing.com/news)                              | No                                                                  |
|                            | News API                                             | API                  | Provides access to news articles from various sources, useful for M&A tracking. | [News API](https://newsapi.org)                                     | No                                                                  |
| **Financial News Websites**| Bloomberg                                            | API/Web Scraping     | Detailed articles on financial news, including M&A activities.                 | [Bloomberg](https://www.bloomberg.com)                              | No                                                                  |
|                            | Reuters                                              | API/Web Scraping     | Reliable source for up-to-date news on mergers and acquisitions globally.      | [Reuters](https://www.reuters.com)                                  | [Reuters RSS](http://feeds.reuters.com/reuters/businessNews)        |
|                            | Financial Times                                      | API/Web Scraping     | In-depth analysis and reports on business and financial markets.               | [Financial Times](https://www.ft.com)                               | [Financial Times RSS](https://www.ft.com/?format=rss)               |
|                            | Handelsblatt                                         | Web Scraping         | German business newspaper providing insights into local M&A activities.        | [Handelsblatt](https://www.handelsblatt.com)                        | [Handelsblatt RSS](https://www.handelsblatt.com/rss)                |
| **Industry-specific Websites** | Mergermarket                                    | Subscription         | Intelligence on M&A deals, specialized in this area.                           | [Mergermarket](https://www.mergermarket.com)                        | No                                                                  |
|                            | PitchBook                                            | Subscription         | Data on private and public capital markets, including M&A transactions.        | [PitchBook](https://pitchbook.com)                                  | No                                                                  |
|                            | S&P Global Market Intelligence                       | Subscription         | Comprehensive data and insights on financial markets, including M&A activities.| [S&P Global](https://www.spglobal.com/marketintelligence/en/)       | No                                                                  |
| **Regulatory and Government Websites** | Unternehmensregister                     | Official Website     | Central platform for legally relevant company information in Germany, including financial statements and merger announcements. | [Unternehmensregister](https://www.unternehmensregister.de)         | No                                                                  |
|                            | Bundesanzeiger                                       | Official Website     | Official gazette of the German government, where companies publish legal announcements, including mergers, acquisitions, and financial statements. | [Bundesanzeiger](https://www.bundesanzeiger.de)                     | No                                                                  |
|                            | BaFin (Federal Financial Supervisory Authority)      | Official Website     | Supervises and regulates financial institutions in Germany, including M&A activities, market disclosures, and financial stability reports. | [BaFin](https://www.bafin.de)                                       | No                                                                  |
|                            | Bundeskartellamt                                     | Official Website     | German Federal Cartel Office overseeing competition, including merger control proceedings and decisions. | [Bundeskartellamt](https://www.bundeskartellamt.de)                 | No                                                                  |
| **Press Release Websites** | PR Newswire                                          | Web Scraping         | Platform for companies to release official press statements.                   | [PR Newswire](https://www.prnewswire.com)                           | [PR Newswire RSS](https://www.prnewswire.com/rss-feeds/)            |
|                            | Business Wire                                        | Web Scraping         | Major press release distribution service.                                      | [Business Wire](https://www.businesswire.com)                       | [Business Wire RSS](https://www.businesswire.com/portal/site/home/rss/) |
|                            | GlobeNewswire                                        | Web Scraping         | Similar to PR Newswire and Business Wire, used for official announcements.     | [GlobeNewswire](https://www.globenewswire.com)                      | [GlobeNewswire RSS](https://www.globenewswire.com/RssFeed)          |
| **Social Media and Professional Networks** | LinkedIn                              | API/Web Scraping     | Companies often announce major deals on their official LinkedIn pages.         | [LinkedIn](https://www.linkedin.com)                                | No                                                                  |
|                            | Twitter                                              | API/Web Scraping     | Official company accounts and financial news profiles often tweet about M&A activities. | [Twitter](https://www.twitter.com)                                  | No                                                                  |
| **German Financial News Websites** | Börsen-Zeitung                               | Web Scraping         | German financial newspaper covering finance, economy, and M&A news.            | [Börsen-Zeitung](https://www.boersen-zeitung.de)                    | [Börsen-Zeitung RSS](https://www.boersen-zeitung.de/rss)            |
|                            | Wirtschaftswoche                                     | Web Scraping         | German weekly business news magazine providing economic and financial news.    | [Wirtschaftswoche](https://www.wiwo.de)                             | [Wirtschaftswoche RSS](https://www.wiwo.de/rss)                     |
|                            | Der Aktionär                                         | Web Scraping         | German finance and investment news website.                                    | [Der Aktionär](https://www.deraktionaer.de)                          | [Der Aktionär RSS](https://www.deraktionaer.de/rss)                 |

## Getting Started

### Prerequisites

Ensure you have the following installed on your machine:

- Python 3.12.x
- pip (Python package installer)

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-repo/ma-monitor.git
    cd ma-monitor
    ```

2. **Set up a virtual environment**:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
 4. **Download the spaCy German language model**:
 ```bash
 python -m spacy download de_core_news_sm
 ```
    
5. **Get your NewsAPI Key**:
    - Go to [NewsAPI](https://newsapi.org/register) and sign up for an API key.
    - Once you have your API key, set it as an environment variable:
        ```bash
        export NEWS_API_KEY="your_newsapi_key"
        ```
6. **Run the data extraction script**:
    ```bash
    python scrapes/newsapi/newsapi.py
    ```

7. **Process the extracted data**:
    ```bash
    python etl/etl.py
    ```
## Example Usage
The `newsapi.py` script fetches German-language news articles related to M&A. The `etl.py` script processes the fetched articles to extract relevant M&A information.

## Future Work
- Integrate additional data sources such as Bundeskartellamt, Unternehmensregister, and Bundesanzeiger.
- Enhance NLP techniques to improve the accuracy of entity extraction and information retrieval.

