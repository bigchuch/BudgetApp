database = {}
class budget:

    

    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.expenditure = 0
        #self.database = {}
        

    def deposit(self):
        deposit_amount = int(input("enter deposit amount %s: " % self.name))
        self.balance += deposit_amount
        print("%d deposited of for %s" %(self.balance, self.name))
        database[self.name]= deposit_amount
        print(database)

    def withdraw(self):
        amount = int(input("how much do you wanna withdraw from %s: " % self.name))
        if database[self.name] >= amount:
            if amount not in range(0,999):
                self.balance -= amount
                self.expenditure += amount
                database[self.name]= self.balance
                #self.database[self.name] = self.database[self.name] - 500
                    

                print(database)
                print("after %d expenditure on %s, %d balance is left" %(self.expenditure,self.name,self.balance))
                   
            else:
                print("only multiples of 1000 is allowed to be withdrawn")
                food.withdraw()
        else:
            print("insufficeint balance")
            food.withdraw()

    def category_balance(self):
         print ("balance for %s is %s " %(self.name, database[self.name]))
         



        #  my_dict = {"username": "XYZ", "email": "xyz@gmail.com", "location":"Mumbai"}
        # print("username :", my_dict['username'])
        # print("email : ", my_dict["email"])
        # print("location : ", my_dict["location"])
        #  #print(budget.database)

    def balance_transfer(self,category_to_transfer):
        self.category_to_transfer = category_to_transfer 
        if category_to_transfer in database: 
            amount_to_transfer = int(input("enter amount to transfer: "))
            #for self.name,details in self.database.items():
            if amount_to_transfer <= database[self.name] :
                updated_old_balance = database[self.name] - amount_to_transfer
                database[self.name] = updated_old_balance
                #budget.budget1 = budget(self.category_to_transfer)
                
                #self.database [category_to_transfer]= amount_to_transfer
                database [self.category_to_transfer]+= amount_to_transfer
                print(database)

            else:
                print("amount to be withdraw is greater than your balance")


        else:
            amount_to_transfer = int(input("enter amount to transfer: "))
        #for self.name,details in self.database.items():
            if amount_to_transfer <= database[self.name] :
                updated_old_balance = database[self.name] - amount_to_transfer
                database[self.name] = updated_old_balance
            #budget.budget1 = budget(self.category_to_transfer)
            
            #self.database [category_to_transfer]= amount_to_transfer
                database [self.category_to_transfer]= amount_to_transfer
                print(database)    
                # alien_0['x_position'] = alien_0['x_position'] + x_increment
                # print(f"New position: {alien_0['x_position']}")
                # print(alien_0)
            
            
         
            
            
            
            
            
            
            else:
                print("amount to be withdraw is greater than your balance")

        
        

    def decison(self):
        print("what other option would you like to do (1) deposit (2) ")

        print

food = budget("food")
entertainment = budget("eba")
#budget2 = budget("")

food.deposit()
entertainment.deposit()

food.withdraw()
entertainment.withdraw()

food.balance_transfer(input("what category do u want to transfer to: "))

food.category_balance()
entertainment.category_balance()


