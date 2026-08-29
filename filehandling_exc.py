"""import csv

# 3 transaction dicts list
transactions = [
    {"description": "Groceries", "amount": 1200, "category": "Food"},
    {"description": "Bus pass", "amount": 500, "category": "Travel"},
    {"description": "Movie", "amount": 350, "category": "Entertainment"},
]

# CSV write
with open("transactions.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["description", "amount", "category"])
    writer.writeheader()
    writer.writerows(transactions)

print("CSV file written successfully!")
# CSV read
with open("transactions.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
"""
# read and write JSON file
import json

transactions = [
    {"description": "Groceries", "amount": 1200, "category": "Food"},
    {"description": "Bus pass", "amount": 500, "category": "Travel"},
    {"description": "Movie", "amount": 350, "category": "Entertainment"},
]

# JSON फाईलमध्ये लिहा
with open("transactions_test.json", "w") as f:
    json.dump(transactions, f, indent=2)

print("JSON file written successfully!")

# JSON फाईल परत वाचा
with open("transactions_test.json", "r") as f:
    loaded = json.load(f)
    print(loaded)

# फरक तपासा — type बघा
print(type(loaded[0]["amount"]))   # <class 'int'> — JSON ने खरा नंबर टाइप ठेवला!