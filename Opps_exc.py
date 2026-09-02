# Exercise 1: BankAccount class
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner      
        self.balance = balance   

    def deposit(self, amount):
        self.balance += amount   
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance!")   
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")


acc = BankAccount("Somnath", 5000)
acc.deposit(2000)      # Deposited 2000. New balance: 7000
acc.withdraw(1000)     # Withdrew 1000. New balance: 6000
acc.withdraw(50000)    # ValueError: Insufficient balance!