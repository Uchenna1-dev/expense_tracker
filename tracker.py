import json

# List to store all expenses (loaded from JSON file)
expenses = []

# Load existing expenses from the JSON file (if it exists)
try:
    with open("expenses.json", "r") as file:
        expenses = json.load(file)
# If the file doesn't exist yet, start with an empty list
except FileNotFoundError:
    expenses = []

# List of accepted categories for expenses
acceptable_categories = ["Groceries", "Bills", "Transport", "Rent", "Other"]


#           MAIN MENU
def main():
    while True:
        print("===================================")
        print("   Welcome to your Expense Tracker  ")
        print("===================================")
        print("Let's start tracking your spending!\n")

        print("Please choose an option: \n1. Add Expense \n2. View Expenses \n3. Exit")

        # User selects a main menu option
        choice = int(input("Enter your choice: "))

        if choice == 1:
            # Add a new expense
            add_expense(expenses, acceptable_categories)

        elif choice == 2:
            # View different kinds of expense summaries
            view_expenses(expenses, acceptable_categories)

        elif choice == 3:
            # Exit the program
            break


#        ADDING EXPENSES
def add_expense(expenses, acceptable_categories):

    # Collect expense details from the user
    group = input("Category of expense: ").title()
    cost = float(input("Expense: "))
    date = input("Date: ")
    short_description = input("Short description: ")

    # If the category is not accepted, automatically assign it to "Other"
    if group not in acceptable_categories:
        group = "Other"

    category_found = False

    # Check if this category already exists in the JSON structure
    for item in expenses:
        if group in item:
            # Add the expense to the existing category list
            item[group].append({
                "cost": cost,
                "date": date,
                "description": short_description
            })
            category_found = True
            break

    # If category doesn't exist yet, create a new category entry
    if category_found == False:
        expenses.append({
            group: [{
                "cost": cost,
                "date": date,
                "description": short_description
            }]
        })

    # Save updated expenses back into the JSON file
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

    print("Expense added successfully!\n")

    return expenses

#       VIEWING EXPENSES

def view_expenses(expenses, acceptable_categories):

    print("Please choose an option: \n1. View all expenses \n2. View expenses by categories \n3. View total spending")

    option = int(input("Option: "))

   
    # 1. VIEW ALL EXPENSES
  
    if option == 1:

        # If there are no expenses at all
        if not expenses:
            print("No expenses found")
        else:
            # Loop through each category and print its expenses
            for item in expenses:
                for category, expense_details in item.items():
                    print(category)
                    print("----")
                    for expense in expense_details:
                        print(
                            expense["cost"],
                            "on",
                            expense["date"],
                            f"({expense['description']})"
                        )

        return expenses

    # 2. VIEW EXPENSES BY CATEGORY
  
    elif option == 2:

        if not expenses:
            print("No expenses found under this category")
            return

        # Ask user which category they want to view
        chosen_category = input("Which category would you like to see: ").title()

        # Validate category input
        while chosen_category not in acceptable_categories:
            print("Invalid category")
            chosen_category = input("Which category would you like to see: ").title()

        # Display expenses under the selected category
        for item in expenses:
            for category, expense_list in item.items():

                if category == chosen_category:
                    print(category)

                    # If the category exists but has no expenses
                    if not expense_list:
                        print("This category has no expense list")
                        return

                    # Print each expense in this category
                    for expense in expense_list:
                        print(
                            expense["cost"],
                            "on",
                            expense["date"],
                            f"({expense['description']})"
                        )

        return expenses

 
    # 3. VIEW TOTAL SPENDING
   
    elif option == 3:
        total = 0

        # If no expenses exist
        if not expenses:
            print("No expenses found!")
            return

        # Sum all expense costs across all categories
        for item in expenses:
            for category, expense_list in item.items():
                for expense in expense_list:
                    total += expense["cost"]

        print(f"Total spending: £{total:.2f}")

        return expenses


#            RUN APP

if __name__ == "__main__":
    main()


