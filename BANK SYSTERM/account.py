# creating the account we first start with th initialize 
class Account:
    def __init__(self,name,balance=50):
        self.name = name
        self.balance = balance

#creating an the deposit function we usse the balance because we are adding the new money to the balance 
    def  deposit(self,amount):
        self.balance += amount
#we are creating a withdrawal funtion we have to create a function special for that because we ahve a mininmun amount to bewitdrawn
    def withdraw(self,amount):
        if self.balance >= amount:
           self.balance -=amount
           return True
        else:
            print('insufficient balance')
            return False
    #checking our balance we dont need anything because we are using the same balance we simply return it

    def get_balance(self):
        return self.balance
    

        