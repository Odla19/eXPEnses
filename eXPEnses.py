# Import necessary modules
import csv
import datetime

# Define the main function
def main():
    # Initialize an empty list to store transactions
    transactions = []

    # Display the main menu
    print("Welcome to eXPEnses!")
    while True:
        print("\nMain Menu:")
        print("1. Add a new transaction")
        print("2. View transaction history")
        print("3. Generate a report")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_transaction(transactions)
        elif choice == "2":
            view_transactions(transactions)
        elif choice == "3":
            generate_report(transactions)
        elif choice == "4":
            print("Exiting eXPEnses. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Function to add a new transaction
def add_transaction(transactions):
    date = input("Enter the date (YYYY-MM-DD): ")
    description = input("Enter the description: ")
    amount = float(input("Enter the amount: "))
    category = input("Enter the category: ")

    transaction = {
        "date": date,
        "description": description,
        "amount": amount,
        "category": category
    }
    transactions.append(transaction)
    print("Transaction added successfully.")

# Function to view the transaction history
def view_transactions(transactions):
    if not transactions:
        print("No transactions found.")
    else:
        print("\nTransaction History:")
        for transaction in transactions:
            print(f"Date: {transaction['date']}, Description: {transaction['description']}, Amount: {transaction['amount']}, Category: {transaction['category']}")

# Function to generate a report
def generate_report(transactions):
    if not transactions:
        print("No transactions found.")
    else:
        # Calculate total income, total expenses, and net balance
        total_income = 0
        total_expenses = 0
        for transaction in transactions:
            if transaction['amount'] >= 0:
                total_income += transaction['amount']
            else:
                total_expenses -= transaction['amount']

        net_balance = total_income - total_expenses

        print("\nFinancial Report:")
        print(f"Total Income: ${total_income:.2f}")
        print(f"Total Expenses: ${total_expenses:.2f}")
        print(f"Net Balance: ${net_balance:.2f}")

        # Save the report to a CSV file
        file_name = f"finance_report_{datetime.date.today().strftime('%Y%m%d')}.csv"
        with open(file_name, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Description", "Amount", "Category"])
            for transaction in transactions:
                writer.writerow([transaction["date"], transaction["description"], transaction["amount"], transaction["category"]])

        print(f"Report saved to {file_name}.")

# Run the main function
if __name__ == "__main__":
    main()