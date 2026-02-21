class Investment:
    def __init__(self, ticker, amount, buy_price):
        self.ticker = ticker
        self.amount = amount
        self.buy_price = buy_price

    def calculate_profit(self, current_price):
        total_profit =  (current_price - self.buy_price) * self.amount
        return total_profit
    
    def report(self, current_price, currency = "USD"):
        profit = self.calculate_profit(current_price)
        if currency == "PHP":
            return f"Ticker: {self.ticker}, Profit: {profit * 56:,.2f} PHP"
        return f"Ticker: {self.ticker}, Profit: {profit:,.2f} USD"    
    
class EquityInvestment(Investment):
    def __init__(self, ticker, amount, buy_price, dividend_yield):
        super().__init__(ticker, amount, buy_price)
        self.dividend_yield = dividend_yield

    def calculate_profit(self, current_price):
        total_profit = ((current_price - self.buy_price) + (self.buy_price * self.dividend_yield)) * self.amount
        return total_profit
    
class CryptoInvestment(Investment):
    def __init__(self, ticker, amount, buy_price, network_fee):
        super().__init__(ticker, amount, buy_price)
        self.network_fee = network_fee

    def calculate_profit(self, current_price):
        total_profit =  ((current_price - self.buy_price) * self.amount) - self.network_fee
        return total_profit
    
class Portfolio:
    def __init__(self):
        self.assets = []
    
    def add_asset(self, asset):
        self.assets.append(asset)

    def get_total_net_worth(self, prices_dict):
        total_portfolio_profit = 0
        for asset in self.assets:
            ticker = asset.ticker
            current_price = prices_dict[ticker]
            profit = asset.calculate_profit(current_price)
            total_portfolio_profit += profit
            return total_portfolio_profit


#--- Testing the Code ---
'''
btc = CryptoInvestment("BTC", 0.5, 40000, 25)
print(btc.report(65000))        # Default USD
print(btc.report(65000, "PHP")) # Overloaded to PHP

spy = EquityInvestment("SPY", 10, 450, 0.015)
print(spy.report(65000))
print(spy.report(65000, "PHP"))
'''
btc = CryptoInvestment("BTC", 0.5, 40000, 25)
spy = EquityInvestment("SPY", 10, 450, 0.015)

my_wealth = Portfolio()

my_wealth.add_asset(btc)
my_wealth.add_asset(spy)

market_prices = {
    "BTC": 68000, 
    "SPY": 520
}

final_profit = my_wealth.get_total_net_worth(market_prices)
print(f"\nTotal Portfolio Profit: ${final_profit:,.2f}")