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
# acc.withdraw(50000)    # ValueError: Insufficient balance!


# Exercise 2: Transaction class + classify() method
class Transaction:
    def __init__(self, description, amount, category):
        self.description = description
        self.amount = amount
        self.category = category

    def classify(self):
        if self.category in ("Food", "Rent"):
            return "Essential"
        elif self.category in ("Travel", "Entertainment"):
            return "Discretionary"
        else:
            return "Unknown"

t1 = Transaction("Groceries", 1200, "Food")
print(t1.classify())   # Essential

t2 = Transaction("Movie", 350, "Entertainment")
print(t2.classify())   # Discretionary