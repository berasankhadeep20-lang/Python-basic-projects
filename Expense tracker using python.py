#Expense tracker using python
#!/usr/bin/env python3
def Expense_tracker():
    import time

    def typewriter_effect(text, delay=0.05):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()

    expenses = []

    def add_expense():
        try:
            amount = float(input("Enter expense amount: "))
            description = input("Enter expense description: ")
            expenses.append((amount, description))
            typewriter_effect("Expense added successfully!")
        except ValueError:
            typewriter_effect("Invalid amount. Please enter a number.")

    def view_expenses():
        if not expenses:
            typewriter_effect("No expenses recorded.")
            return
        typewriter_effect("Expenses:")
        for idx, (amount, description) in enumerate(expenses, start=1):
            typewriter_effect(f"{idx}. ${amount:.2f} - {description}")

    while True:
        typewriter_effect("\nExpense Tracker Menu:")
        typewriter_effect("1. Add Expense")
        typewriter_effect("2. View Expenses")
        typewriter_effect("3. Exit")
        choice = input("Choose an option (1-3): ")

        try:
            if choice == '1':
                add_expense()
            elif choice == '2':
                view_expenses()
            elif choice == '3':
                typewriter_effect("Exiting Expense Tracker. Goodbye!")
                break
            else:
                typewriter_effect("Invalid choice. Please try again.")
        except KeyboardInterrupt:
            typewriter_effect("\nExiting Expense Tracker. Goodbye!")
            break
        except Exception as e:
            typewriter_effect(f"An error occurred: {e}")
Expense_tracker()