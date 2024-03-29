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
        To be complaint with that principle we need to remove varying parameters from pay method which is "security_code" in our example. And recieve thier values in initialization phase of class

    4. Interface segregation: segregate interfaces as per the requirements of the program, 
        rather than one general-purpose implementation

        Violation:
        In our code, PaymentProcess interface has the auth_sms method to be implemented. However, 
        the method is not implemented in all its descendants, specifically in CreditPayment.
        It raises an exception violating both Interface segregation and Liskov substitution.

        Resolving:
        We have two options:
            1) Creating more specific interfaces
            2) Create a separate class for the authentication feature and compose it with Payment class
    
    5. Dependency Inversion: Removing dependency between two concrete classes, rather move dependency type to more abstract type like interfaces.
        
        Violation: 
        In our code, we have dependency among SMSAuth and DebitPayment, PayPalPayment.

        Resolving:
        We will create a new interface Authorizer and change type hint to that interface
        Of course, in python, it doesn't change anything but only increases readability.
        That way we can later pass other authorizer-type objects to PaymentProcessor classes.

