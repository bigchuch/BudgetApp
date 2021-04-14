
class budget:

    database = {}

    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.expenditure = 0
        #self.database = {}
        

    def deposit(self):
        deposit_amount = int(input("enter deposit amount %s: " % self.name))

        self.balance += deposit_amount

        print("%d deposited of for %s\n" %(self.balance, self.name))

        self.database[self.name]= deposit_amount
        #print(database)

    def withdraw(self):
        amount = int(input("how much do you wanna withdraw from %s: " % self.name))
        if self.database[self.name] >= amount:
            
            if amount not in range(0,999):

                self.balance -= amount

                self.expenditure += amount

                self.database[self.name]= self.balance
    
                print(self.database)
                
                print("after %d witdrawal from %s budget, %d balance is left\n" %(self.expenditure,self.name,self.balance))
                   
            else:
                print("only multiples of 1000 is allowed to be withdrawn\n")
                self.withdraw()
        else:
            print("insufficeint balance")
            self.withdraw()

    def category_balance(self):
        
        print ("balance for %s is %s \n" %(self.name, self.database[self.name]))
         

    def balance_transfer(self,category_to_transfer):

        self.category_to_transfer = category_to_transfer 

        if category_to_transfer in self.database: 

            amount_to_transfer = int(input("enter amount to transfer: "))
            
            if amount_to_transfer <= self.database[self.name]:

                updated_old_balance = self.database[self.name] - amount_to_transfer

                self.database[self.name] = updated_old_balance
       
                self.database [self.category_to_transfer]+= amount_to_transfer
                print("successfully transfered %d from %s budget to %s budget\n" %(amount_to_transfer,self.name, self.category_to_transfer))
                
                print(self.database)

            else:
                print("amount to be withdraw is greater than your balance\n")


        else:
            amount_to_transfer = int(input("enter amount to transfer: "))
        
            if amount_to_transfer <= self.database[self.name] :

                updated_old_balance = self.database[self.name] - amount_to_transfer

                self.database[self.name] = updated_old_balance
                     
                self.database [self.category_to_transfer]= amount_to_transfer

                print("successfully transfered %d from %s budget to %s budget\n" %(amount_to_transfer,self.name, self.category_to_transfer))
                
                print(self.database)

               

            else:
                print("amount to be withdraw is greater than your balance\n")

        
        

    def decison(self):
        print("******** WELCOME TO MY BUDGET APP ********")
        print("what other option would you like to do (1) deposit (2) ")

        print

def main():
    food = budget("rice")
    entertainment = budget("wedding")
    #budget2 = budget("")

    food.deposit()
    entertainment.deposit()

    food.withdraw()
    entertainment.withdraw()

    food.balance_transfer(input("what category do u want to transfer to: "))

    food.category_balance()
    entertainment.category_balance()


main()
