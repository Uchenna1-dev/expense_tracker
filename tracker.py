import json

expenses = []
#reload expenses file each time program runs, code defensively using try and except
try:
    with open("expenses.json", "r") as file:
        expenses = json.load(file)

except FileNotFoundError:
    expenses = []

#create a category list and check to see if user input is in the list, if not then put in Other category.
acceptable_categories = ["Groceries", "Bills", "Transport","Rent", "Other"]

# start with a welcome text 
def main():
    
    while True:
        
        print("===================================")
        print("   Welcome to your Expense Tracker  ")
        print("===================================")
        print("Let's start tracking your spending!\n")

        print("Please choose an option: \n1. Add Expense \n2. View Expenses \n3. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            expenses = add_expense(expenses, acceptable_categories)
             #print back to confirm expense added
            
    
        elif choice == 2:
            expenses = view_expenses(expenses, acceptable_categories)
            
        elif choice == 3:
            break
            
            
def add_expense(expenses, acceptable_categories):

    group = input("Category of expense: ").title()
    cost = float(input("Expense: "))
    date = input("Date: ")
    short_description = input("Short description: ")

    # STEP 1 — Check if category is allowed
    if group not in acceptable_categories:
        group = "Other"
    
    category_found = False
    # STEP 2 — Try to add expense to an existing category in JSON
    for item in expenses:
        if group in item:
            item[group].append({
                "cost": cost,
                "date": date,
                "description": short_description
            })
            category_found = True
            break
        
    if category_found == False:
        # STEP 3 — Category not found → create it
        expenses.append({
            group: [{
                "cost": cost,
                "date": date,
                "description": short_description
            }]
        })

    # Save to JSON
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

    print("Added")

    return expenses

def view_expenses(expenses, acceptable_categories):

    print("Please choose an option: \n1. View all expenses \n2. View expenses by categories \n3. View total spending")

    option = int(input("Option: "))

    if option == 1:

        if not expenses:
            print("No expenses found")

        else:
            for item in expenses:
                for category, expense_details in item.items():
                    print(category)
                    print("----")
                    for expense in expense_details:
                        print(expense["cost"], end= ' ')
                        print ("on", end=' ')
                        print(expense["date"], end= ' ')
                        print(f"({expense['description']})")
        return expenses

#view expense by categories
    elif option == 2:
        if not expenses:
            print("No expenses found under this category")
            return

        chosen_category = input("Which category would you like to see: ").title()
    

        while chosen_category not in acceptable_categories:
            print("Invalid category")
            chosen_category = input("Which category would you like to see: ").title()

        
        for item in expenses:

            for category, expense_list in item.items():

                if category == chosen_category:
                    print(category)

                    if not expense_list:
                        print("This category has no expense list")
                        return
                        
                    for expense in expense_list: # change this to a one liner later
                        print(expense["cost"], end= ' ')
                        print ("on", end=' ')
                        print(expense["date"], end= ' ')
                        print(f"({expense['description']})")
        
        return expenses

#View total spending
    elif option == 3:
        total = 0

        if not expenses:
            print("No expenses found!")
            return
        
        for item in expenses:
            for category, expense_list in item.items():
                for expense in expense_list:
                    total += expense["cost"]
                
        print(f"Total spending: £{total:.2f}")
    
        return expenses        
    
if __name__ == "__main__":
    main()
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


# ===============================
#           MAIN MENU
# ===============================
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


# ===============================
#        ADDING EXPENSES
# ===============================
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


# ===============================
#       VIEWING EXPENSES
# ===============================
def view_expenses(expenses, acceptable_categories):

    print("Please choose an option: \n1. View all expenses \n2. View expenses by categories \n3. View total spending")

    option = int(input("Option: "))

    # ------------------------------------
    # 1. VIEW ALL EXPENSES
    # ------------------------------------
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

    # ------------------------------------
    # 2. VIEW EXPENSES BY CATEGORY
    # ------------------------------------
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

    # ------------------------------------
    # 3. VIEW TOTAL SPENDING
    # ------------------------------------
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


# ===============================
#            RUN APP
# ===============================
if __name__ == "__main__":
    main()


