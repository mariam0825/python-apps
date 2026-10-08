class Account(object):
     # to continue without doing anything use (pass,...)
     # __init__ is a magic method
    def __init__(self,name: str,) -> None:
        self.name = name.lower()
        self.balance = 0


    def deposit(self,amount:float):
        if amount < 0:
            raise ValueError("Depoist cannot be negative")
        self.balance += amount
    
    def withdraw(self,amount:float):
        if amount > self.balance:
            raise ValueError("You cannot withdraw more you have ")
        self.balance -= amount
        


#account = Account(name:"Eniife")
#account = Account(name:"Winifred")
