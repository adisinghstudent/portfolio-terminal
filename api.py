import requests

def fetch_stock_price(api_key, symbol):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    try:
        # Get the latest time interval
        latest_interval = list(data['Time Series (1min)'].keys())[0]
        # Get the closing price for the latest interval
        price = float(data['Time Series (1min)'][latest_interval]['4. close'])
        return price
    except KeyError:
        print(f"Error fetching data for {symbol}")
        return None



portfolio = {}

def add_stock(portfolio, stock, shares):
    if stock in portfolio:
        portfolio[stock] += shares
    else:
        portfolio[stock] = shares

def get_shares(portfolio, stock):
    return portfolio.get(stock, 0)

def display_portfolio(portfolio):
    for stock, shares in portfolio.items():
        print(f"{stock}: {shares} shares")

def calculate_portfolio_value(portfolio, api_key):
    total_value = 0
    for stock, shares in portfolio.items():
        price = fetch_stock_price(api_key, stock)
        if price is not None:
            total_value += shares * price
    return total_value


def display_portfolio_value(portfolio, api_key):
    value = calculate_portfolio_value(portfolio, api_key)
    print(f"Total portfolio value: ${value:.2f}")

def main():
    api_key = 'lesson #never hardcode your api key in here'  # Replace with your Alpha Vantage API key
    while True:
        print("\n1. Add stock")
        print("2. Get shares of a stock")
        print("3. Display portfolio")
        print("4. Display portfolio value")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            stock = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares: "))
            add_stock(portfolio, stock, shares)
        elif choice == '2':
            stock = input("Enter stock symbol: ").upper()
            shares = get_shares(portfolio, stock)
            print(f"You have {shares} shares of {stock}")
        elif choice == '3':
            display_portfolio(portfolio)
        elif choice == '4':
            display_portfolio_value(portfolio, api_key)
        elif choice == '5':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
