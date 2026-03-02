from abc import ABC, abstractmethod

class Business(ABC):
    @abstractmethod
    def sell_product(self, product_name, price, quantity):
        pass

class Bakery(Business):
    def __init__(self, business_name):
        self.business_name = business_name

    def sell_product(self, product_name, quantity, price):
        total_revenue = price * quantity
        print(f"""{self.business_name} sold {quantity} {product_name} for a total of {total_revenue}""")
    
blue_eyed_baker = Bakery("Blue Eyed Baker")
blue_eyed_baker.sell_product("Dark Chocolate", 2, 4)