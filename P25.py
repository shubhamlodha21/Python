#Function Name:Prime
#Input:11
#Output:11 is Prime Number
#Description:program which accept one number form user and Check is Prime or Not
#Date: 02/08/2021
#Author: Shubham Lodha


def prime(no1):
    sum=0
    for i in range(2,no1,1):
        if(no1%i==0):
            return 1        
    return 0

def main():
    no1=int(input("Enter a Number"))
    bRet=prime(no1)
    if(bRet==1):
        print(no1,"is Not a Prime Number")
    else:
        print(no1,"is Prime Number")

if __name__=="__main__":
    main()