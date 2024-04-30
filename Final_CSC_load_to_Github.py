#Final
#CSC 401
#Lauren Blakeley


##This Python program will simulate a simple ATM machine. Any user with an account must be able to enter a pin number and select
##from a menu of options: Deposit, Withdrawal, Balance, Get Information, and Quit. It is implied that any one user has only one account
##where these options can be executed. The ATM needs to properly and regularly communicate with the user. 
##The ATM needs to get information on current accounts from a file(accounts.txt). 
##Each line of the file contains a first name, last name, and the account balance.

##import random to generate random integers. 
import random 
##import datetime for use in the exit function as the date of the transaction must 
    ##be printed on the receipt.
from datetime import datetime

##Create a class called account with two parameters, balance and accountNumber.
##The default value for balance is 0 and the default balance for accountNumber is -1.
class Account:
    accountNumber = 0

##If the parameter accountNumber is the default value, set the class variable accountNumber
    ##to a randomly generated number between 10000000 and 99999999. Elif- the parameter accountNumber
    ##is greater than or equal to 10000000 then the class variable accountNumber is set to the 
    ##value of the passed parameter.
    ##Then, create a class variable transLog that will be an empty list and a class variable
    ##balance to store the account balance.
    def __init__(self, balance = 0, accountNumber = -1):
        if accountNumber == -1:
            self.accountNumber = random.randint(10000000, 99999999)
        elif accountNumber >= 10000000:
            self.accountNumber = accountNumber
        self.transLog = []
        self.balance = balance

    ##Create and return 6 functions: getAccountNumber, getBalance, getTransactions, 
        ##Deposit, Withdraw, and addTransaction. 

    def getAccountNumber(self):
        return self.accountNumber
    
    def getBalance(self):
        return self.balance 
    
    def getTransactions(self):
        return self.transLog
    
    def deposit(self, amount):
        self.balance += amount
        self.addTransaction(f"Deposit: +${amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds, please withdraw an amount less than or equal to your balance.")
            return
        self.balance -= amount 
        self.addTransaction(f"Withdrawal: -${amount}")

    def addTransaction(self, transaction):
        self.transLog.append(transaction)


##Create a class called User. This will be a subclass of class Account, thus User(Account),
        ##and will implement functions: createPin(), getName(), and getPin().
        ##Constructor in initialize will take three parameters, name (no default value),
        ##balance (will be passed to the constructor of the super class),
        ##accountNumber (will be passed to the constructor of the super class, default value is -1)
class User(Account):
    def __init__(self, name, balance, accountNumber=-1):
        super().__init__(balance, accountNumber)
        self.name = name
        self.createPin()

    ##Create and return 3 functions: createPin, getName, and getPin.
    def createPin(self):
        self.pin = random.randint(1000,9999)

    def getName(self):
        return self.name
    
    def getPin(self):
        return self.pin
    
##Create a class called ATM. This class will have an initialization function, a function to 
    ##read accounts from a file, an authorize function, a displayMenu function that contains a 
    ##while loop to iterate through options 1-5 in the menu, and an exit function.
class ATM:
    def __init__(self):
        self.accounts = []
        self.readAccountsFromFile()
        self.authorize()

    def readAccountsFromFile(self):
        with open("accounts.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                name = f"{data[0]}"
                balance = float(data[1])
                user = User(name, balance)
                self.accounts.append(user)
                print(f"Created user: {user.getName()} with PIN: {user.getPin()}")

    def authorize(self):
        invalid_attempts = 0
        while invalid_attempts < 3:
            pin = int(input("Enter your PIN: "))
            for user in self.accounts:
                if pin == user.getPin():
                    print(f"Welcome, {user.getName()}!")
                    self.displayMenu(user)
                    return
            invalid_attempts += 1
            print("Invalid PIN, try again.")
        print("You have performed too many invalid logins. Goodbye.")

    def displayMenu(self, user):
        while True:
            print("\nMenu:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Balance")
            print("4. Account Info")
            print("5. Quit")
            choice = input("Enter your choice: ")
            try:
                choice = int(choice)
                if choice not in [1, 2, 3, 4, 5]:
                    raise ValueError
            except ValueError:
                print("Invalid choice. Enter 1, 2, 3, 4, or 5. Try again.")
                continue

            if choice == 1:
                amount = float(input("Enter the amount to deposit: "))
                user.deposit(amount)
            elif choice == 2:
                amount = float(input("Enter the amount to withdraw: "))
                user.withdraw(amount)
            elif choice == 3:
                print(f"Current balance: ${user.getBalance()}")
            elif choice == 4:
                print(f"Account Number: {user.getAccountNumber()}")
                print(f"Account Balance: ${user.getBalance()}")
                print(f"User Name: {user.getName()}")
            elif choice == 5:
                confirm = input("Are you sure you want to quit? (Y/N): ").lower()
                if confirm == 'y':
                    self.exit(user)
                    return
                

    def exit(self, user):
        print("\nReceipt:")
        print("Transactions:")
        for transaction in user.getTransactions():
            print(transaction)
        print("Date:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print("Customer Name:", user.getName())
        print("Remaining Balance:", user.getBalance())
        print("Goodbye!")

##Create a function called main which takes no parameters. This instantiates the ATM class.
        ##Instantiation is the process where you generate an instance of a class. It creates an 
        ##object from the mapping done via class. Essentially bringing the class to life and 
        ##making it real for use.
def main():
    atm = ATM()

if __name__ == "__main__":
    main()