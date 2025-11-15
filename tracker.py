import json

expenses = []
#create a category list and check to see if user input is in the list, if not then put in Other category.
acceptable_categories = ["Groceries", "Bills", "Transport","Rent", "Other"]

# start with a welcome text 
def main():
    global expenses
    while True:
        #reload expenses file each time program runs, code defensively using try and except
        try:
            with open("expenses.json", "r") as file:
                expenses = json.load(file)

        except FileNotFoundError:
            expenses = []

        print("===================================")
        print("   Welcome to your Expense Tracker  ")
        print("===================================")
        print("Let's start tracking your spending!\n")

        print("Please choose an option: \n1. Add Expense \n2. View Expenses \n3. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_expense()
             #print back to confirm expense added
            
    
        elif choice == 2:
            view_expenses()
            
        elif choice == 3:
            break
            
            
def add_expense():
    global expenses

    group = input("Category of expense: ").title()
    cost = float(input("Expense: "))
    date = input("Date: ")
    short_description = input("Short description: ")

    # STEP 1 — Check if category is allowed
    if group not in acceptable_categories:
        group = "Other"

    # STEP 2 — Try to add expense to an existing category in JSON
    for item in expenses:
        for key, value in item.items():
            if key == group:
                value.append({
                    "cost": cost,
                    "date": date,
                    "description": short_description
                })
                break
        else:
            continue
        break
    else:
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

 #expense saved to memory 
    with open("expenses.json","w") as file:
        json.dump(expenses, file, indent = 4)

    print("Added")

#should have a continue or go back to the main menu option
    return

def view_expenses():

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


    
    
if __name__ == "__main__":
    main()


