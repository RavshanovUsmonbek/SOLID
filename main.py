'''
    1. Applying first principle: Single responsibility principle
        
        Violation:
        Class Order contains responsibility for both containning orders and processing payments 
        which violates the principle above. 
        
        Resolving:
        Thus we seperate out pay method to seperate class named PaymentProcessor. 
        Moreorver, the pay methods itself is not responsible for single item, instead it's both handling
        debit and credit card payments. Likewise, we create seperate methods for each payment type.
    
    2. Open/Closed principle: Open to extensions, closed to modifications

        Violation:
        In our example, if we want to add a new type of payment method, then we need to modify existing
        PaymentProcessor class. And that violates Open/Closed principle. What we want instead is having structure of 
        classes that allows as adding new class which hold a new functionality which new payment method in our case

        Resolving:
        For that, we need to create a general PaymentProcessor interface from which each payment method classes inherit.
        That way we complain for the principle above. 

        We will add a new payment method - PayPalPayment
    
    3. Liskov substitution: objects of a superclass shall be replaceable with objects 
        of its subclasses without breaking the application.
    
        Violation: 
        In our code, PayPalPayment class's pay method is not dependent on security code,
        but instead email_address. If we change the parameter name to email_address from security_code than it won't 
        be compatible with PaymentProcessor interface's pay method signature. That tells us that our code is not complaint
        with Liskov substitution principle.

        Resolving: 
        To be complaint with that principle we need to remove varying parameters from pay method
        which is "security_code" in our example. And recieve thier values in initialization phase of class

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
    def pay(self, order):
        pass


class DebitPayment(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code
    
    def pay(self, order):
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"
    

class CreditPayment(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status="paid"


class PayPalPayment(PaymentProcessor):
    def __init__(self, email_address):
        self.email_address = email_address

    def pay(self, order):
        print("Processing paypal payment type")
        print(f"Verifying email address: {self.email_address}")
        order.status="paid"


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

processor = PayPalPayment("ravshanov@gmail.com")
print(order.total_price())
processor.pay(order)

