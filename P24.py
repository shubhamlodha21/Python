#Function Name:Addfactorial
#Input:10
#Output:Addition of FActorial is: 8
#Description:program which accept one number form user and return addition of its factors
#Date: 02/08/2021
#Author: Shubham Lodha

def AddFactorial(no1):
    sum=0
    for i in range(1,no1,1):
        if(no1%i==0):
            sum=sum+i        
    return sum

def main():
    no1=int(input("Enter a Number"))
    iRet=AddFactorial(no1)
    print("Addition of FActorial is:",iRet)

if __name__=="__main__":
    main()