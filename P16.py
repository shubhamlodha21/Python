#Function Name:ChkSum
#Input:-50
#Output: -50 is Negative
#Description: Accept Number from user and return positive,negative or zero
#Date: 03/08/2021
#Author: Shubham Lodha

def ChkNum(no1):
    if(no1==0):
        print(no1,"is Zero")
    elif(no1>0):
        print(no1,"is Positive")
    else:
        print(no1,"is Negative")
    

def main():
    no1=int(input("Enter a Number"))
    ChkNum(no1)
    
if __name__=="__main__":
    main()
