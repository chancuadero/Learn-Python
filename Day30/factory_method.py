from abc import ABC, abstractmethod

class Customer(ABC):
    @abstractmethod
    def make_payment(self, price):
        pass

class RewardsMember(Customer):
    def make_payment(self, price):
        print(f"""Total price for rewards member is ${price * .90}, which is 10% off""")
    
class NewCustomer(Customer):
    def make_payment(self, price):
        print(f"""Total price for new customer is ${price}""")

class Checkout:
    def _get_customer(self, customer_type):
        if customer_type == "Rewards Member":
            return RewardsMember()
        elif customer_type == "New Customer":
            return NewCustomer()
        
    def complete_transaction(self, customer_type, price):
        customer = self._get_customer(customer_type)
        customer.make_payment(price)

chan = Checkout()
chan.complete_transaction("New Customer", 12)

