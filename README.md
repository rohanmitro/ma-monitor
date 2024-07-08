# ma-monitor
# Mergers & Acquisitions Monitoring Project

## Overview

This project aims to monitor and extract information on mergers and acquisitions (M&A) in Germany. The focus is to gather relevant data from multiple sources, including news aggregators, financial news websites, industry-specific platforms, regulatory and government websites, press release services, and social media. The extracted data will be processed, stored, and analyzed to provide valuable insights into the M&A landscape.

## Project Goals

- **Automate Data Collection**: Use web scraping, APIs, and RSS feeds to gather M&A information from various sources.
- **Data Processing**: Apply Natural Language Processing (NLP) and regular expressions to extract specific details from the collected data.
- **Data Storage**: Store the processed data in a structured format for easy querying and analysis.
- **Data Analysis and Visualization**: Generate reports and dashboards to visualize M&A trends and activities.

## Data Sources

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

- Python 3.x
- pip (Python package installer)
- Jupyter Notebook (optional but recommended for interactive data exploration)

### Installation

1. **Clone the Repository**
   ```sh
   git clone https://github.com/yourusername/ma-monitor.git
   cd ma-monitor
   ```
2. **Install Dependencies**
    ```sh
    pip install -r requirements.txt
    ```

