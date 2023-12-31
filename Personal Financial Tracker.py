import datetime
import time
import threading

class Transaction:
    def __init__(self, name, amount, type):

        self.name = name
        self.amount = amount
        self.type = type

class Account:
    def __init__(self):

        self.expenses = []
        self.incomes = []

    def add_expenses(self, name, amount, type):

        expense = Transaction(name, amount, type)
        self.expenses.append(expense)
    
    def total_expenses(self):

        total = 0
        for expense in self.expenses:
            total += expense.amount
        return total

    def display_expense_list(self):

        for loss in self.expenses:
            print(f"Name: {loss.name}, Expense Amount: {loss.amount}, Type: {loss.type}")
    
    def add_receipts(self, name, amount, type):

        income = Transaction(name, amount, type)
        self.incomes.append(income)
    
    def total_income(self):

        total = 0
        for receipt in self.incomes:
            total += receipt.amount
        return total
    
    def display_receipt_list(self):

        for earnings in self.incomes:
            print(f"Name: {earnings.name}, Expense Amount: {earnings.amount}, Type: {earnings.type}")
    
    def difference(self):
        return self.total_income() - self.total_expenses()

class Clock(threading.Thread):
    def __init__ (self):

        super().__init__()
        self.daemon = True
        self.present_time = ""
    
    def run(self):
        while True:
            self.present_time = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
            time.sleep(1)

def menu():

    personal_finance = Account()

    clock = Clock()
    clock.start()

    while True:

        print(f"Current Time: {clock.present_time}")
        print("Please choose 1 of the following options.")
        print("1. Add an expense")
        print("2. Add an earning")
        print("3. View Personal Expense List")
        print("4. View Personal Earning List")
        print("5. Calculate the difference between your Expenses and Earnings")
        print("6. Quit")

        try:
            choice = int(input("Please enter a number from 1-6: "))

        except ValueError:
            print("Invalid Input. Please enter a valid number that is within 1-6.")

        if choice == 1:
            print()
            name = input("Enter the collector's name: ")
            type = input("Enter the expense type: ")
            expense_amount = float(input("Enter the expense amount: "))
            personal_finance.add_expenses(name, expense_amount, type)
            print()

        elif choice == 2:
            print()
            name = input("Enter the payer's name: ")
            type = input("Enter the earnings type: ")
            earnings_amount = float(input("Enter the earnings amount: "))
            personal_finance.add_receipts(name, earnings_amount, type)
            print()
        
        elif choice == 3:
            print()
            print("Here are your expenses: ")
            print()
            personal_finance.display_expense_list()
            print()
            print(f"Here is the total amount: {personal_finance.total_expenses()}")
        
        elif choice == 4:
            print()
            print("Here are your earnings: ")
            print()
            personal_finance.display_receipt_list()
            print()
            print(f"Here is the total amount: {personal_finance.total_income()}")
        
        elif choice == 5:
            print()
            print("Here is the difference between your earnings and expenses:", personal_finance.difference())

        elif choice == 6:
            print()
            print("Exit")
            break

        else:
            print()
            print("Please select a valid option")
            print()

if __name__ == "__main__":

    print("Welcome.")
    menu()