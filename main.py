

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

