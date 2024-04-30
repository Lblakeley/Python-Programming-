 #Assignment 7
#CSC 401
#Lauren Blakeley

##Two classes need to be developed and they will be called Account and Transit Card. Create the class Account first, this is where 
##the money is stored to pay for bus and train fare. Fares are subtracted from the Account every time you use your card and 
##100 frequent rider points are then earned.If balances are insufficient, you will not be able to board a bus or train. 
##A new transit card is purchased for $5 and a card can be purchased with up to $100 in transit value on it. 
##You can add money to your account at anytime. You cannot add more than $100 per transaction and any cardholder's account 
##may never exceed $350 in value. 

##Create class Account
class Account:
    name = ""
    transitCards = []

    ##name is set to class variable and the empty list 'transitCards' will store all of the TransitCards associated with the account.
    def __init__(self, name):
        self.name = name
        self.transitCards = []

    ##getBalance will return the balance for the account. One account can have multiple transit cards so this step is necessary
    ##to see the full balance of any one account.
    def getBalance(self):
        total_balance = sum(card.getBalance() for card in self.transitCards)
        return total_balance
    
    ##like getBalance, getPoints returns the points balance for the account. Since one account can have multiple transit cards, 
    ##this step needs to be taken to see the full points balance across all cards linked to any one account. 
    def getPoints(self):
        total_points = sum(card.riderPoints for card in self.transitCards)
        return total_points
    
    ##getName just returns the name of the Account holder.
    def getName(self):
        return self.name
    
    ##takes the parameter 'card' which is the TransitCard and appends it to the TransitCard list.
    def addCard(self, card):
        self.transitCards.append(card)

    ##returns a new account object with all of the class attributes added together. 
    def __add__(self, newAccount):
        new_account = Account(self.name)
        new_account.transitCards = self.transitCards + newAccount.transitCards
        return new_account
    
##Create class TransitCard
class TransitCard:

    ##initializes a transit card that may have a balance amount up to $100 and a default amount of $5.
    ##also, create a class variable called riderPoints with a default value of 0.
    def __init__(self, amount = 5, riderPoints = 0):
        if amount > 100:
            raise ValueError("Amount is > 100.00")
        self.balance = amount
        self.riderPoints = riderPoints

    ##subtracts fare amount from card balance as long as card balance is greater than 0, if not, raise ValueError.
        ##add 100 points to riderPoints after subtracting the cost of the fare from the balance.
    def ride(self, fare):
        if self.balance <= 0:
            raise ValueError("Card balance is 0 or negative; ride is denied")
        elif self.balance < fare:
            self.balance = 0
        else:
            self.balance -= fare
        self.riderPoints += 100

    ##take amount as input. Raise ValueError is the amount attempted to add is greater than $100. 
    ##raise ValueError if the amount added will make the total card balance greater than $350.
    ##if both conditions are met (amount added is less than $100 and total amount on card will be less than $350)
        ##then add amount to balance.
    
    def addValue(self, amount):
        if amount > 100:
            raise ValueError("Amount is > 100.00")
        elif self.balance + amount > 350:
            raise ValueError("Card balance will be greater than 350.00; request is denied")
        else:
            self.balance += amount

    ##return the balance, takes no input.
    def getBalance(self):
        return self.balance
    
    ##returns a statement that informs the user what the card balance is.
    def __repr__(self):
        return f"The card balance is {self.balance}"
    
    ##adds two values together, creating a new instance of the TransitCard class.
    def __add__(self, other):
        total_balance = self.balance + other.balance
        return TransitCard(total_balance)
    
    ##statement will return as true if two cards have equal values for both balance and riderPoints. 
    def __eq__(self, other):
        return self.balance == other.balance and self.riderPoints == other.riderPoints
    
    ##opposite of statement above, will return as trye if two cards are not equal across all attributes.
    def __ne__(self, other):
        return not self.__eq__(other)
    
    ##returns true if one card's balance is larger than another card's balance.
    def __gt__(self, other):
        return self.balance > other.balance
    
    ##returns true if one card's balance is greater than or equal to another card's balance. 
    def __ge__(self, other):
        return self.balance >= other.balance
    
    ##returns true if one card has a lower balance than another card.
    def __lt__(self, other):
        return self.balance < other.balance
    
    ##returns true if one card has a balance lower than or equal to another card's.
    def __le__(self, other):
        return self.balance <= other.balance

