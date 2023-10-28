# Stock Price Checker and News Notifier

This Python script allows you to check the latest stock price for a specific company and
receive news articles related to that company if the price has significantly changed.
In this example, it's configured to check the stock price of Tesla Inc (TSLA).

## Prerequisites

Before using this script, make sure you have the following:

- Python installed on your system.
- The requests library, which you can install using `pip`:
  ```
  pip install requests
  ```

## Usage

1. Obtain API Keys:
   - You need an API key from Alpha Vantage to access stock price data. Replace `API_KEY` in the script with your Alpha Vantage API key.
   - You also need an API key from News API to access news articles. Replace `NEWS_API` in the script with your News API key.

2. Run the Script:
   - Execute the script in your Python environment.

3. Output:
   - The script will check the stock price for Tesla Inc (TSLA) and calculate the
     percentage difference between the current and previous closing prices.
   - If the percentage difference is greater than 5% or less than -5%,
     the script will fetch news articles related to Tesla Inc and print the headlines, descriptions, and URLs for the top 3 articles.

## Configuration

You can easily customize this script for different stocks or companies by changing the values of the following variables in the script:

- `STOCK`: The stock symbol you want to monitor (e.g., TSLA for Tesla Inc).
- `COMPANY_NAME`: The name of the company you're interested in (e.g., Tesla Inc).

## Disclaimer

This script is provided for educational and informational purposes only.
It may require a valid subscription or API keys for the services it uses.
The stock market is subject to fluctuations, and no guarantees are made regarding the accuracy or timeliness of the data provided.

---
