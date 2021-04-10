class budget:
# Create a Budget class that can instantiate objects based on different budget 
# categories like food, clothing, and entertainment. These objects 
# should allow for
# 1.  Depositing funds to each of the categories
# 2.  Withdrawing funds from each category
# 3.  Computing category balances
# 4.  Transferring balance amounts between categories

# Push your code to GitHub, and submit the repo link.
    database = {}

    def __init__(self, name):
        self.name = input("what would you like to budget on: ")
        self.balance = 0
        self.expenditure = 0
        

    def deposit(self):
        deposit_amount = int(input("enter deposit amount: "))
        self.balance += deposit_amount
        print("%d deposited of for %s" %(self.balance, self.name))
        budget.database[self.name]= [deposit_amount]
        print(budget.database)

    def withdraw(self):
        amount = int(input("how much do you wanna withdraw: "))
        for self.name,details in budget.database.items():
            if details[0] > amount:
                #if amount > 100:
                    self.balance -= amount
                    self.expenditure += amount
                    budget.database[self.name]= [self.balance]
                    print(budget.database)
                    print("after %d expenditure on %s, %d balance is left" %(self.expenditure,self.name,self.balance))
                   
                #else:
                    #print("only multiples of 100 is allowed")
            else:
                print("insufficeint balance")


    def category_balance(self):
         print ("balance is %s " % budget.database[self.name])
         #print(budget.database)

    def balance_transfer(self):
        print("enter transfer details")
        

    def decison(sef):
        print("what other option would you like to do (1) deposit (2) ")
        print

food1 = budget("food")
food2 = budget("food")

food1.deposit()
food2.deposit()
#food1.withdraw()
#food1.category_balance()
