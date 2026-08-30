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


# Class Attributes vs Instance Attributes
class Transaction:
    essential_categories = ("Food", "Rent")   # ← Class attribute —  objects SHARED

    def __init__(self, description, amount, category):
        self.description = description   # ← Instance attribute —  object 
        self.amount = amount
        self.category = category

t1 = Transaction("Groceries", 1200, "Food")
t2 = Transaction("Movie", 350, "Entertainment")

print(Transaction.essential_categories)   # ("Food", "Rent") —  access 
print(t1.essential_categories)            