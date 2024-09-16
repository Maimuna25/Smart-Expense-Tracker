from expense_tracker import add_expenses, view_expenses
from insights import expense_insights
from expense_prediction import run_prediction


def menu():
    while True:
        print("\nExpense Tracker Menu")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Expense Insights")
        print("4. View Predictions")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_expenses()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            expense_insights()
        elif choice == '4':
            run_prediction()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

