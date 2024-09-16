import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import os

# Path to the expense CSV file
EXPENSE_FILE = 'data/expenses.csv'

def load_and_prepare_data(expense_file):
    # Check if the expense file exists
    if not os.path.exists(expense_file):
        print(f"{expense_file} not found.")
        return None, None

    # Load the expenses CSV file
    expenses = pd.read_csv(expense_file)

    # Convert 'Date' to datetime and sort by date
    expenses['Date'] = pd.to_datetime(expenses['Date'])
    expenses.sort_values('Date', inplace=True)

    # Feature Engineering: Convert Date to ordinal (numeric format for regression)
    expenses['Date_Ordinal'] = expenses['Date'].apply(lambda date: date.toordinal())

    # Define features (X) and target (y)
    X = expenses[['Date_Ordinal']]  # Use Date as independent variable
    y = expenses['Amount']  # Amount as the target/dependent variable

    return X, y

def train_and_predict(X, y):
    # Split the data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    # Create and train the regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict the test set
    y_pred = model.predict(X_test)

    # Visualize the result
    plt.plot(X_test, y_test, color='blue', label='Actual')
    plt.plot(X_test, y_pred, color='red', label='Predicted')
    plt.xlabel('Date')
    plt.ylabel('Amount Spent')
    plt.title('Expense Prediction Over Time')
    plt.legend()
    plt.show()

def run_prediction():
    # Load the data
    X, y = load_and_prepare_data(EXPENSE_FILE)

    if X is None or y is None:
        print("Error: No data to process.")
        return

    # Train the model and predict
    train_and_predict(X, y)

