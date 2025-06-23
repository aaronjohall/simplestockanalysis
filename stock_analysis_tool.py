# Simple Stock Analysis Tool using yfinance

import yfinance as yf
import pandas as pd

# Retrieving stock from ticker and calculating functions.
def get_stock_data(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    return {
        'symbol': info.get('symbol'),
        'longName': info.get('longName'),
        'sector': info.get('sector'),
        'currentPrice': info.get('currentPrice'),
        'marketCap': info.get('marketCap'),
        'trailingPE': info.get('trailingPE'),
        'forwardPE': info.get('forwardPE'),
        'priceToBook': info.get('priceToBook'),
        'profitMargins': info.get('profitMargins'),
        'returnOnEquity': info.get('returnOnEquity'),
        'beta': info.get('beta'),
        'dividendYield': info.get('dividendYield'),
        '52WeekChange': info.get('52WeekChange')
    }

def print_summary(data):
    print("\n--- Stock Summary ---")
    for key, value in data.items():
        print(f"key{key}: {value}")

def main():
    ticker = input("Enter Stock Ticker (e.g. COST): ").upper()
    try:
        stock_data = get_stock_data(ticker)
        print_summary(stock_data)
    except Exception as e:
        print(f"Error Retrieving data: {e}")

if __name__ == "__main__":
    main()