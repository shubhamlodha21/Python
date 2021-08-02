#Function Name:Arithmetic
#Input:10  20
#Output:

#Addition is: 30       
#Substractions is: -10 
#Multiplication is: 200
#Division is 0.5

#Description:Accept Number from user and perform arithmetic operations
#Date: 02/08/2021
#Author: Shubham Lodha


def Add(no1,no2):
    return no1+no2

def Sub(no1,no2):
    return no1-no2

def Mult(no1,no2):
    return no1*no2

def Div(no1,no2):
    return no1/no2

def main():
    no1=int(input("Enter First Number"))
    no2=int(input("Enter Second Number"))

    iRet=Add(no1,no2)
    print("Addition is:",iRet)

    iRet=Sub(no1,no2)
    print("Substractions is:",iRet)

    iRet=Mult(no1,no2)
    print("Multiplication is:",iRet)

    iRet=Div(no1,no2)
    print("Division is",iRet)

if __name__=="__main__":
    main()

