# finance_tracker.py


print("Welcome to the Personal Finance Tracker!")

# Dictionary will store expenses.
# The keys will be categories (strings), and the values will be lists of tuples.
# Each tuple will represent an expense: (description_string, amount_float)


expenses = {}

def add_expense(expenses_data):
    
    print("\n-- Add New Expense 💵 --")
    description = input("Enter expense description: ").strip() # .strip() removes whitespace
    category = input("Enter category: ").strip()
    
    # Exceptions and validation for amount input
    while True:
        amount_input = input("Enter amount: ").strip()
        try:
            amount = float(amount_input)
            if amount <= 0:
                print("Amount must be a positive number. try again")
            else:
                break 
        except ValueError:
            print("Invalid amount. Please enter a number (ex = 12.50)")
        except Exception as e:
            
            print(f"An unexpected error occurred: {e}. Please try again.")

    # Convert category to lowercase for consistency
    category = category.lower()

    # If the categorynot in dictionary then create a new list for it
    if category not in expenses_data:
        expenses_data[category] = []
    
    # Add the expenses as tuple to the category's list
    expenses_data[category].append((description, amount))
    print("Expense added 💵 ✅")

def view_expenses(expenses_data):
    
    print("\n-- All Expenses --")
    if not expenses_data: #Dictionary is empty
        print("No expenses")
        return

    # Finder:Iterate thru category and expenses
    for category, expense_list in expenses_data.items():
        print(f"Category: {category.capitalize()}") # Capitalize category for display
        if not expense_list:
            print("  No expenses in this category.")
        else:
            for description, amount in expense_list:
                print(f"  - {description}: ${amount:.2f}") # Format amount to 2 decimal places

def view_summary(expenses_data):
    
    print("\n-- Expense Summary by Category --")
    if not expenses_data: # Check if the dictionary is empty
        print("No expenses recorded yet.")
        return

    # new dictionary to hold the total for each category
    category_totals = {}
    for category, expense_list in expenses_data.items():
        total_amount = sum(amount for _, amount in expense_list) # Sum the amounts from tuples
        category_totals[category] = total_amount
    
    # Print the summary
    for category, total in category_totals.items():
        print(f"{category.capitalize()}: ${total:.2f}") # Capitalize and format

def main_menu():
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Summary")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            view_summary(expenses)
        elif choice == '4':
            print("bye ✌️!")
            break 
        else:
            print("Invalid option! ❌ Please choose a number from 1 to 4.")


if __name__ == "__main__":
    main_menu()