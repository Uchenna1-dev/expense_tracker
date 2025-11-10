import json

#create a list to store all expenses
expenses =[
    {"Groceries": [] },
    {"Transport": [] },
    {"Bills": [] },
]

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
            add_expense()
            print(expenses)
    

        if choice == 2:
            #view expenses
            pass

        elif choice == 3:
            break
            
            


def add_expense():
    #user to input expense
    group = input("Category of expense: ")  #need to think of how to make it case sensitive
    cost = float(input("Expense: "))
    date = input("Date: ")
    short_description = input("Short description: ")
    match = False

    for item in expenses:
        for category, expense in item.items():
            if group.lower() == category.lower():
                expense.append({"cost": cost, "date": date, "description": short_description})
                match = True

    if match == False:
        expenses.append({group: [{"cost": cost, "date": date, "description": short_description}]})

 #print back to confirm expense added
    print("Added")

 #expense saved to memory 
    with open("expenses.json","w") as file:
        json.dump(expenses, file)
#reload expenses file each time program runs, code defensively using try and except
    try:
        with open("expenses.json", "r") as file:
        expenses = json.load(file)

    except FIleNotFoundError:
        expenses = []

#should have a continue or go back to the main menu option
    return


    

if __name__ == "__main__":
    main()


