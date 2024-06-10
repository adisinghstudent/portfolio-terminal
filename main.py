#define data storage for the portfolio, data type dictionary(map), portfolio here is a keyword use to get that date.
portfolio = {}



# For simplicity, using static prices. In a real application, fetch prices from an API.
stock_prices = {
    'AAPL': 150.00,
    'GOOGL': 2800.00,
    'MSFT': 300.00
}

#add_stock function to add stock where we need three parameters, portofolio, type of stock and the amount of shares.
def add_stock(portfolio, stock, shares):
    if stock in portfolio:
        portfolio[stock] += shares
    else:
        portfolio[stock] = shares

def remove_stock(portfolio, stock, shares):
    if stock in portfolio:
        portfolio[stock] -= shares
    else:
        portfolio[stock] = shares

#get_shares function looks at the dictionary portofolio and gets the amount of stock
def get_shares(portfolio, stock):
    return portfolio.get(stock, 0)

#calculate_portfolio_value gives the total value.
def calculate_portfolio_value(portfolio, stock_prices):
    total_value = 0
    #iterates through each stock in portfolio and adds up the total value
    for stock, shares in portfolio.items():
        total_value += shares * stock_prices.get(stock, 0)
    return total_value

#display function for stocks and shares
def display_portfolio(portfolio):
    for stock, shares in portfolio.items():
        print(f"{stock}: {shares} shares")

#display function for total value
def display_portfolio_value(portfolio, stock_prices):
    value = calculate_portfolio_value(portfolio, stock_prices)
    print(f"Total portfolio value: ${value:.2f}")

#main function
def main():
    while True:
        print("\n0. Add stock")
        print("1. Remove stock")
        print("2. Get shares of a stock")
        print("3. Display portfolio")
        print("4. Display portfolio value")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '0':
            stock = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares: "))
            add_stock(portfolio, stock, shares)
        if choice == '1':
            stock = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares: "))
            remove_stock(portfolio, stock, shares)
        elif choice == '2':
            stock = input("Enter stock symbol: ").upper()
            shares = get_shares(portfolio, stock)
            print(f"You have {shares} shares of {stock}")
        elif choice == '3':
            display_portfolio(portfolio)
        elif choice == '4':
            display_portfolio_value(portfolio, stock_prices)
        elif choice == '6':
            print("Thanks for using the portofolio manager! ")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
