#Function Name:Divisible5
#Input:50
#Output:True
#Description:Check whether a Given Number is divisble by 5 or not 
#Date: 03/08/2021
#Author: Shubham Lodha

def Divisble5(no1):
    if(no1%5==0):
        print("True")
    else:
        print("False")
    

def main():
    no1=int(input("Enter a Number"))
    Divisble5(no1)
    
if __name__=="__main__":
    main()
