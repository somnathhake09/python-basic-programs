#Instance Methods
class Transaction:
    def __init__(self, description, amount, category):
        self.description = description
        self.amount = amount
        self.category = category

    def display(self):   #  instance method 
        print(f"{self.description}: {self.amount} ({self.category})")

t1 = Transaction("Groceries", 1200, "Food")
t1.display()   # Groceries: 1200 (Food)