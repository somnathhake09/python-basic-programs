#Exercises (सराव)
# reate a list of 5 expense amounts. Add one more, remove one, then print the sorted list.
#ate a tuple ("Rent", 8000, "Housing"). Try to change the amount — observe and explain the error.
#  #en cats = ["Food", "Travel", "Food", "Bills", "Travel"], convert it to a set and print how many unique categories there are.
#uild a dictionary for one transaction with keys: description, amount, category, date. Then print just the amount using the key.
#reate a list of 3 transaction dictionaries (like the nested example above). Loop through them and print the total of all amounts.
#opy pitfall: create a list x = [1,2,3], assign y = x, append 4 to y. Print x. Then redo it properly using .copy() so x is unaffected.

expense =[1000,999,500,2000,1500]
expense.append(2500)
expense.remove(999)
expense.sort()
print(expense)

housing_expense = ("Rent", 8000, "Housing")
housing_expense[1] = 8500  # This will raise an error because tuples are immutable
print(housing_expense)
cats = ["Food","Travel","Food","Bills","Travel"]
s = set(cats)
print(s)

transaction ={
    "description": "Grocery",
    "amount": 100,
    "category": "Food",
    "datwe": "2023-10-01"
}
print(transaction["amount"])
s =[{ "description": "Grocery", "amount": 100 }, { "description": "Rent", "amount": 8000 },{ "description": "Bills", "amount": 500 }]
print(s["amount"])

x = [1, 2, 3]   # a list is created, x points to it
y = x           # y points to the SAME list, not a new one
y.append(4)     # we add 4 — but we're adding to the ONE shared list
print(x)        # x sees the change too!

a = [1, 2, 3]
b = a.copy()    # b is now a NEW, separate list with the same values
b.append(4)     # this only affects b
print(a)        # a is untouched
print(b)