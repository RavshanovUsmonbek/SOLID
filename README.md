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

        Resolving: To be complaint with that principle we need to remove varying parameters from pay method
        which is "security_code" in our example. And recieve thier values in initialization phase of class
