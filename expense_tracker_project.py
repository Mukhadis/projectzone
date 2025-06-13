# This is a simple command-line program that allows user to:

# Add an expense to a pretend bank account. If there are no expenses return there message stating there is nothing

import csv
from datetime import datetime

expenses = []

def main():
    while True:
        decision = input("To log and expenses, please press 1, to view expenses please press 2, to end press 3\n")
        if decision == "1":
           add_expense()
        elif decision == "2":
           view_expenses()
        elif decision == "3":
           print("Have a great day")
           break
        else:
           print('This is an invalid request')     

def add_expense():
    # Desc takes in the reason of the inputted expense
    desc = input("Please state the reason for this expense: ")
    try:
        # Value takes in a float, the number to be recorded for the expense
        value = float(input("Please state the value of this expense: "))

    except ValueError:
        # Will run this code if there is an error from adding an invalid float
        print("This is an invalid amount")
        return
     # Date will take in inputed date from the user
    date = input("Please input todays date YYYY-MM-DD: ")
    if not date:
        # If the user does not input a date the programme will pull it from the date.time function
        date = datetime.today().strftime('%Y-%m-%d')
    
    # Appends all this information and prints
    expenses.append({"description": desc, "value":value, "date": date})
    print("The following expenses were added:\n", expenses)

def view_expenses():
    if not expenses:
        # If there are no recorded expenses return the following statement
        print("You have no expenses")
        return
    # Print the expenses
    for e in expenses:
        print(f"{e['date']} - {e['description']} - {e['value']}")

if __name__ == "__main__":

    main()