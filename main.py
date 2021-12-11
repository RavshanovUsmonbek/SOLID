'''
    1. Applying first principle: Single responsibility principle
        
        Class Order contains responsibility for both containning orders and processing payments 
        which violates the principle above. 
        Thus we seperate out pay method to seperate class named PaymentProcessor. 
        Moreorver, the pay methods itself is not responsible for single item, instead it's both handling
        debit and credit card payments. Likewise, we create seperate methods for each payment type.

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


class PaymentProcessor:
    def pay_debit(self, order, security_code):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"
    
    def pay_credit(self, order, security_code):
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        order.status="paid"


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

processor = PaymentProcessor()
print(order.total_price())
processor.pay_debit(order, "0989795")

