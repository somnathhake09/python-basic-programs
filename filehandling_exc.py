import csv

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