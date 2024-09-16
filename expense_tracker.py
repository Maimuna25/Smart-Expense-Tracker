import pandas as pd
import os

EXPENSE_FILE = 'data/expenses.csv'


def add_expenses():
    # Get user input
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category (Food, Transport, Entertainment, etc.): ")
    amount = float(input("Enter the amount: "))
    description = input("Enter a brief description: ")

    # Create a DataFrame from the data
    expense_data = pd.DataFrame([{
        'Date': date,
        'Category': category,
        'Amount': amount,
        'Description': description
    }])

    # If file exists, append to it; else create new with headers
    if os.path.exists(EXPENSE_FILE):
        expense_data.to_csv(EXPENSE_FILE, mode='a', header=False, index=False)
    else:
        expense_data.to_csv(EXPENSE_FILE, index=False)

    print("Expense added successfully!")


def view_expenses():
    # Check if file exists
    if os.path.exists(EXPENSE_FILE):
        expenses = pd.read_csv(EXPENSE_FILE)
        print(expenses)
    else:
        print("No expenses recorded yet.")

