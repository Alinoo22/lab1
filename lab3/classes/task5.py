class bank_account:
    def __init__(self, owner, balance=0):  
        self.owner = owner  
        self.balance = balance  

    def deposit(self, amount):  
        if amount > 0: 
            self.balance += amount  
            print("deposited {amount}. new balance: {self.balance}")
        else:
            print("deposit amount must be positive.") 

    def withdraw(self, amount):  
        if amount <= self.balance:  
            self.balance -= amount  
            print("withdrew {amount}. new balance: {self.balance}")
        else:
            print("insufficient balance!")  

#Let's try it with example
account = bank_account("John", 1000) 
account.deposit(500) 
account.withdraw(300)  
account.withdraw(2000)  