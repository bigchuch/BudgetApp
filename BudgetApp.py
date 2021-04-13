#import randrange
class budget:

    # database = {}

    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.expenditure = 0
        self.database = {}
        

    def deposit(self):
        deposit_amount = int(input("enter deposit amount %s: " % self.name))
        self.balance += deposit_amount
        print("%d deposited of for %s" %(self.balance, self.name))
        self.database[self.name]= deposit_amount
        print(self.database)

    def withdraw(self):
        amount = int(input("how much do you wanna withdraw from %s: " % self.name))
        if self.database[self.name] >= amount:
            if amount not in range(0,999):
                self.balance -= amount
                self.expenditure += amount
                self.database[self.name]= self.balance
                #self.database[self.name] = self.database[self.name] - 500
                    

                print(self.database)
                print("after %d expenditure on %s, %d balance is left" %(self.expenditure,self.name,self.balance))
                   
            else:
                print("only multiples of 1000 is allowed to be withdrawn")
                budget1.withdraw()
        else:
            print("insufficeint balance")
            budget1.withdraw()

    def category_balance(self):
         print ("balance for %s is %s " %(self.name, self.database[self.name]))
         



        #  my_dict = {"username": "XYZ", "email": "xyz@gmail.com", "location":"Mumbai"}
        # print("username :", my_dict['username'])
        # print("email : ", my_dict["email"])
        # print("location : ", my_dict["location"])
        #  #print(budget.database)

    def balance_transfer(self,category_to_transfer):
        self.category_to_transfer = category_to_transfer 
        amount_to_transfer = int(input("enter amount to transfer: "))
        #for self.name,details in self.database.items():
        if amount_to_transfer <= self.database[self.name] :
            updated_old_balance = self.database[self.name] - amount_to_transfer
            self.database[self.name] = updated_old_balance
            #budget.budget1 = budget(self.category_to_transfer)
            
            #self.database [category_to_transfer]= amount_to_transfer
            self.database [self.category_to_transfer]= amount_to_transfer
            print(self.database)

            
                # alien_0['x_position'] = alien_0['x_position'] + x_increment
                # print(f"New position: {alien_0['x_position']}")
                # print(alien_0)
            
            
         
            
            
            
            
            
            
        else:
            print("amount to be withdraw is greater than your balance")

        
        

    def decison(self):
        print("what other option would you like to do (1) deposit (2) ")

        print

budget1 = budget("food")
# budget2 = budget("eba")
#budget2 = budget("")

budget1.deposit()
#budget2.deposit()

budget1.withdraw()
#budget2.withdraw()

budget1.balance_transfer(input("what category do u want to transfer to: "))

budget1.category_balance()
#budget2.category_balance()


