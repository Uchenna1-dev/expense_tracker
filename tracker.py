# start with a welcome text 
def main():
    print("===================================")
    print("   Welcome to your Expense Tracker  ")
    print("===================================")
    print("Let's start tracking your spending!\n")

    print("Please choose an option: \n1. Add Expense \n2. View Expenses \n3. Exit")

    choice = int(input("Enter your choice: "))

    while choice == 1:
        # add expenses 
        pass

    if choice == 2:
        #view expenses
        pass

    elif choice == 3:
        #exit
        pass

if __name__ == "__main__":
    main()

def add_expenses():
    #user to input expense
    expense = float(input("Expense: "))
    #expense saved to memory 
  
    #and added to list of expenses
    #print back to confirm expense added
    #should have a continue or go back to the main menu option
