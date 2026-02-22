#creating a parent class Property
class Property:
    #defining __init__ method with attributes of address and square_meters
    def __init__(self, address, square_meters):
        self.address = address
        self.square_meters = square_meters

    #get_property_details method returning an f string.
    def get_property_details(self):
        return f"Property at {self.address}, Size: {self.square_meters} sqm"
    
#creating a parent class Investment
class Investment:
    def __init__(self, ticker, amount, buy_price):
        self.ticker = ticker
        self.amount = amount
        self.buy_price = buy_price

    def get_financial_summary(self):
        return(f"Ticker: {self.ticker}, Total Cost: ${self.amount * self.buy_price}")
    
#creating a child class derived from both parent class
class TokenizedRealEstate(Property, Investment):
    def __init__(self, address, square_meters, ticker, amount, buy_price):
        Property.__init__(self, address, square_meters)
        Investment.__init__(self, ticker, amount, buy_price)

    #added a full_report method to call the combined methods from both parent classes.
    def full_report(self):
        return f"{self.get_property_details()}. {self.get_financial_summary()}"
    
# Create a tokenized apartment in New York
token_prop = TokenizedRealEstate(
    address="5th Ave, NYC", 
    square_meters=120, 
    ticker="NY-APT", 
    amount=100, 
    buy_price=500
)
print(token_prop.full_report())