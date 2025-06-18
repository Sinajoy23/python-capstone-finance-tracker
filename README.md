# python-capstone-finance-tracker

# Personal Finance Tracker

This is a personal finance tracker built in Python. It allows users to record their expenses, categorize them, and view summaries of their spending.

I used a dictionary called expenses. This dictionary is where all financial data entries will be stored. The keys of this dictionary are expense categories (like "food," "clothing"), and the values will be a list of tuples. Each tuple will hold a (description, amount) for an expense within that category. The keys will be categories (strings), and the values will be lists of tuples. Each tuple will represent an expense: (description_string, amount_float)





## How to Run the Script

1.  **download the `finance_tracker.py` from https://github.com/Sinajoy23/python-capstone-finance-tracker/blob/main/finance_tracker.py
    
2.  **Run the Python script:**
    ```bash
    python finance_tracker.py
    

## Python Concepts Used

* Control Structures: `if`, `elif`, `else` statements
* Loops: `while` loops for the main menu and input validation
* Functions: Modularizing code {`add_expense`, `view_expenses`, `view_summary`, `main_menu`}
* String Operations: `strip()`, `lower()`, and `capitalize()`
* Lists: Storing multiple expenses within a category
* Dictionaries: Storing expenses categorized by key
* Tuples: Storing `(description, amount)` for individual expenses.
* Exception Handling: `try-except` blocks for error management (e.g., `ValueError` for non-numeric input)
