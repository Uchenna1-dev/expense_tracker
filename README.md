## Expense Tracker (Python)

A simple, beginner-friendly command-line application for tracking everyday spending.
This project allows users to record expenses, view them by category, and calculate total spending.
All expenses are saved to a JSON file so the data is kept between program runs.

## Features
1. Add an Expense

Enter the category, cost, date, and a short description.

Categories include: Groceries, Bills, Transport, Rent, and Other.

If the user enters a category that is not recognised, the expense is automatically placed in “Other”.

Expenses are stored in a JSON file to make them persistent.

2. View Expenses

Users can choose from:

View all expenses
Displays every category and every recorded purchase.

View expenses by category
Shows expenses only in the selected category.

View total spending
Outputs the sum of all recorded expenses, formatted to two decimal places.

3. Persistent Storage

All expenses are saved to a JSON file (expenses.json).

The program loads the file when it starts, allowing users to continue where they left off.

## How It Works

The program uses:

A list of dictionaries to organise expenses.

A set of predefined accepted categories.

A simple menu system that lets the user navigate between options.

A clean and readable structure, with separate functions for:

- Adding expenses

- Viewing expenses

- Viewing totals

- Saving and loading data

## File Structure
expense-tracker


── expenses.json        
  #Stores all saved expenses

── expense_tracker.py   
  #Main application code

## How to Run

Ensure you have Python installed.

Clone or download this repository.

Navigate into the folder and run the application:

python tracker.py

Follow the on-screen menu.

## Future Improvements

This project can be expanded with features such as:

Editing or deleting expenses

Filtering expenses by date

Exporting reports

Adding monthly or weekly summaries