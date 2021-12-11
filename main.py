'''
    1. Applying first principle: Single responsibility principle
        
        Class Order contains responsibility for both containning orders and processing payments 
        which violates the principle above. 
        
        Thus we seperate out pay method to seperate class named PaymentProcessor. 
        Moreorver, the pay methods itself is not responsible for single item, instead it's both handling
        debit and credit card payments. Likewise, we create seperate methods for each payment type.
    
    2. Open/Closed principle: Open to extensions, closed to modifications

        In our example, if we want to add a new type of payment method, then we need to modify existing
        PaymentProcessor class. And that violates Open/Closed principle. What we want instead is having structure of 
        classes that allows as adding new class which hold a new functionality which new payment method in our case

        For that, we need to create a general PaymentProcessor interface from which each payment method classes inherit.
        That way we complain for the principle above. 

        We will add a new payment method - PayPalPayment

'''

class Order:
    items = []
    quantities = []
    prices = []
    status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)
    
    def total_price(self):
        return sum(map(lambda p, q: p*q, self.prices, self.quantities))



import abc

class PaymentProcessor(abc.ABC):
    @abc.abstractmethod
    def pay(self, order, security_code):
        pass


class DebitPayment(PaymentProcessor):
    def pay(self, order, security_code):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"
    

class CreditPayment(PaymentProcessor):
    def pay(self, order, security_code):
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        order.status="paid"


class PayPalPayment(PaymentProcessor):
    def pay(self, order, security_code):
        print("Processing paypal payment type")
        print(f"Verifying security code: {security_code}")
        order.status="paid"


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

processor = PayPalPayment()
print(order.total_price())
processor.pay(order, "0989795")

