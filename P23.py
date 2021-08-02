#Function Name:Factorial
#Input:5
#Output:FActorial is 120
#Description:program which accept one number from user and return its factorial.
#Date: 02/08/2021
#Author: Shubham Lodha


def Factorial(no1):
    multi=1
    for i in range(2,no1+1,1):
        multi=multi*i
    return multi

def main():
    no1=int(input("Enter a Number"))
    iRet=Factorial(no1)
    print("FActorial is:",iRet)

if __name__=="__main__":
    main()