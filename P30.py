#Function Name:AddDigits
#Input:123654
#Output:21
#Description:Accept number from user and return addition of its Digits
#Date: 05/08/2021
#Author: Shubham Lodha

def AddDigits(no):
    sum=0
    while(no!=0):
        iDigit=no%10
        sum=sum+iDigit
        no//=10
    return sum

def main():
    no=int(input("Enter a Number"))
    iRet=AddDigits(no)
    print("Addition of Digits is",iRet)

if __name__=="__main__":
    main()