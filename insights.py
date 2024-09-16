import pandas as pd
import os
import matplotlib.pyplot as plt

EXPENSE_FILE = 'data/expenses.csv'

def expense_insights():
    if not os.path.exists(EXPENSE_FILE):
        print("No expenses recorded yet.")
        return

    # Load the expenses
    expenses = pd.read_csv(EXPENSE_FILE)

    # 1. Total Expenses
    total_spent = expenses['Amount'].sum()
    print(f"Total spent: £{total_spent:.2f}")

    # 2. Expenses by Category
    category_spent = expenses.groupby('Category')['Amount'].sum()
    print("\nExpenses by Category:")
    print(category_spent)

    # 3. Plotting Spending Trends (Daily)
    expenses['Date'] = pd.to_datetime(expenses['Date'])
    daily_spending = expenses.groupby('Date')['Amount'].sum()

    plt.figure(figsize=(10, 5))
    plt.plot(daily_spending.index, daily_spending.values, marker='o', linestyle='-')
    plt.title('Daily Spending Over Time')
    plt.xlabel('Date')
    plt.ylabel('Amount Spent (£)')
    plt.grid(True)
    plt.show()

# Call the function
expense_insights()
