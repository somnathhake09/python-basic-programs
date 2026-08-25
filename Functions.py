# Write a function calculate_remaining(income, expenses)that returns income - expenses.
def calculate_remaining(income, expenses):
    print("Remaining:", income - expenses)

calculate_remaining(5000, 3000)

# Write a function classify_expense(category, essential_list)with a default argument essential_list=["Food", "Rent"] that returns "Essential"or "Discretionary".
def classify_expense(category, essential_list=["Food", "Rent"]):
    if category in essential_list:
        return "Essential"
    else:
        return "Discretionary"

print(classify_expense("Food"))             
print(classify_expense("Travel"))         
print(classify_expense("Movies", ["Movies", "Games"]))  

# Write a function total_spending(*amounts)using *argsthat returns the sum.
def total_spending(*amounts):
    return sum(amounts)
print(total_spending(100, 200, 300))

#Write a function print_transaction(**details)using **kwargsthat prints each key-value pair nicely formatted.
def print_transaction(**details):
    for key, value in details.items():
        print(f"{key}:{value}")
print_transaction(description="Grocery", amount=100, category="Food", date="2023-10-01")

# Write a lambda that takes a transaction dict and returns its "amount"— then use it inside sorted()to sort a list of transaction dicts by amount, highest first (hint: reverse=True).
transaction = [
    {"description": "Grocery", "amount": 100},
    {"description": "Entertainment", "amount": 50},
    {"description": "Utilities", "amount": 200}
]
sorted_transactions = sorted(transaction, key=lambda x: x["amount"], reverse=True)
print(sorted_transactions)

# Scope challenge: predict the output of the incomeexample above before running it, then confirm.
income = 5000

def calculate_remaining(income, expenses):
    income = 4000
    print("Local income inside function:", income) 

calculate_remaining(5000, 3000)
print("Global income outside function:", income)     