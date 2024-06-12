portfolio = {}

import os
import requests
from datetime import datetime

def fetch_stock_price(api_key, symbol):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    try:
        latest_interval = list(data['Time Series (1min)'].keys())[0]
        price = float(data['Time Series (1min)'][latest_interval]['4. close'])
        return price
    except KeyError:
        print(f"Error fetching data for {symbol}")
        return None

def calculate_portfolio_value(portfolio, api_key):
    total_value = 0
    for stock, details in portfolio.items():
        shares = details['shares']
        purchase_date = details['purchase_date']
        current_price = fetch_stock_price(api_key, stock)
        if current_price is not None:
            total_value += shares * current_price
    return total_value

def add_stock(portfolio, stock, shares, purchase_date):
    portfolio[stock] = {'shares': shares, 'purchase_date': purchase_date}

def get_shares(portfolio, stock):
    return portfolio.get(stock, {'shares': 0})['shares']

def get_purchase_date(portfolio, stock):
    return portfolio.get(stock, {'purchase_date': 'N/A'})['purchase_date']

def display_portfolio(portfolio):
    for stock, details in portfolio.items():
        print(f"{stock}: {details['shares']} shares purchased on {details['purchase_date']}")

def display_portfolio_value(portfolio, api_key):
    value = calculate_portfolio_value(portfolio, api_key)
    print(f"Total portfolio value: ${value:.2f}")

def remove_stock(portfolio, stock, shares_to_remove):
    if stock in portfolio:
        current_shares = portfolio[stock]['shares']
        if shares_to_remove >= current_shares:
            del portfolio[stock]
            print(f"Removed all shares of {stock} from the portfolio.")
        else:
            portfolio[stock]['shares'] -= shares_to_remove
            print(f"Removed {shares_to_remove} shares of {stock}. Remaining shares: {portfolio[stock]['shares']}")
    else:
        print(f"{stock} not found in the portfolio.")

def main():
    api_key = os.getenv('ALPHA_VANTAGE_API_KEY')
    if not api_key:
        print("API key not found. Please set the ALPHA_VANTAGE_API_KEY environment variable.")
        return
    
    portfolio = {}
    while True:
        print("\n1. Add stock")
        print("2. Remove shares of a stock")
        print("3. Get shares of a stock")
        print("4. Display portfolio")
        print("5. Display portfolio value")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            stock = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares: "))
            purchase_date = input("Enter purchase date (YYYY-MM-DD): ")
            try:
                datetime.strptime(purchase_date, '%Y-%m-%d')
                add_stock(portfolio, stock, shares, purchase_date)
            except ValueError:
                print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
        elif choice == '3':
            stock = input("Enter stock symbol: ").upper()
            shares = get_shares(portfolio, stock)
            purchase_date = get_purchase_date(portfolio, stock)
            print(f"You have {shares} shares of {stock} purchased on {purchase_date}")
        elif choice == '4':
            display_portfolio(portfolio)
        elif choice == '5':
            display_portfolio_value(portfolio, api_key)
        elif choice == '2':
            stock = input("Enter stock symbol: ").upper()
            shares_to_remove = int(input("Enter number of shares to remove: "))
            remove_stock(portfolio, stock, shares_to_remove)
        elif choice == '6':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

