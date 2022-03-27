#Banking Application with some facilities

import sys

class Bank(object):
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance

    def Deposite(self,amount):
        self.balance+=amount
        return self.balance

    def Withdraw(self,amount):
        if amount>self.balance:
            print("Balance Amount is Less, No Withdraw Possible !!")
        else:
            self.balance-=amount
        return self.balance

name=input("Enter Username:")
b=Bank(name)

while(True):
    print("For Deposite -d, Withdraw -w, Exit -e")
    choice=str(input("Enter Choice:"))

    if choice=="e" or choice=="E":
        print("Thanks for Using Application")
        sys.exit()
    
    elif choice=="D" or choice=="d":
        amt=float(input("Enter Amount to Deposite:"))
        print("Balance After Depositing is:",b.Deposite(amt))

    elif choice=="W" or choice=="w":
        amt=float(input("Enter Amount to Withdraw:"))
        print("Balance After Withdraw is:",b.Withdraw(amt))
    
    else:
        print("You have Entered Wrong Option !!")