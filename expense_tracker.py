
expenses = []

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))

    expense = {
        "name": name,
        "amount": amount
    }

    expenses.append(expense)
    print("Expense added successfully!")

def show_expenses():
    total = 0

    print("\n===== EXPENSE DETAILS =====")

    if len(expenses) == 0:
        print("No expenses found.")
        return

    for expense in expenses:
        print(expense["name"], ":", expense["amount"])
        total += expense["amount"]

    print("Total Expenses:", total)

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        show_expenses()
    elif choice == "3":
        print("Thank you!")
        break
    else:
        print("Invalid choice")
