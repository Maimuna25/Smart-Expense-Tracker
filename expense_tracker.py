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
        # Load the expenses CSV file
        expenses = pd.read_csv(EXPENSE_FILE)

        # Displaying the original data
        print("\n--- All Expenses ---")
        print(expenses)

        # Sorting options
        print("\n--- Sorted Data Options ---")
        print("1. Sort by Date")
        print("2. Sort by Category")
        print("3. Sort by Amount")

        sort_option = input("Choose an option to sort (1/2/3): ")

        if sort_option == '1':
            # Sort by date
            expenses['Date'] = pd.to_datetime(expenses['Date'])
            sorted_expenses = expenses.sort_values(by='Date')
        elif sort_option == '2':
            # Sort by category
            sorted_expenses = expenses.sort_values(by='Category')
        elif sort_option == '3':
            # Sort by amount
            sorted_expenses = expenses.sort_values(by='Amount', ascending=False)
        else:
            print("Invalid option. Displaying unsorted data.")
            sorted_expenses = expenses

        print("\n--- Sorted Expenses ---")
        print(sorted_expenses)

        # Summary statistics
        total_spent = expenses['Amount'].sum()
        average_spent = expenses['Amount'].mean()

        print(f"\nTotal Spent: {total_spent}")
        print(f"Average Amount Spent: {average_spent}")

        # Filter by category
    while True:
        filter_option = input("\nDo you want to filter by a specific category? (yes/no): ").lower()
        if filter_option == 'yes':
            category_filter = input("Enter the category to filter by: ")
            filtered_expenses = expenses[expenses['Category'].str.contains(category_filter, case=False, na=False)]

            if not filtered_expenses.empty:
                print(f"\n--- Expenses in Category: {category_filter} ---")
                print(filtered_expenses)
            else:
                print(f"\nNo expenses found in the category: {category_filter}")
        elif filter_option == 'no':
            break
    else:
        print("No expenses recorded yet.")



