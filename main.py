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


class SMSAuth:
    authorized = False

    def verify_code(self, code):
        print(f"Verification SMS code {code}")
        self.authorized = True
    
    def is_authorized(self):
        return self.authorized


class DebitPayment(PaymentProcessor):
    def __init__(self, security_code, authorizer: SMSAuth):
        self.security_code = security_code
        self.authorizer = authorizer
    
    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
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
    def __init__(self, email_address, authorizer: SMSAuth):
        self.email_address = email_address
        self.authorizer = authorizer
    
    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Processing paypal payment type")
        print(f"Verifying email address: {self.email_address}")
        order.status="paid"



order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)
print(order.total_price())

authorizer = SMSAuth()
processor = DebitPayment("098786", authorizer)
authorizer.verify_code(895453)
processor.pay(order)

