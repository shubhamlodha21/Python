# Check whether given number is prime or not
def ChkPrime(n):
    for i in range (2,n):
        if(n%i)==0:
            return 1
    return 0

iNo=int(input("Enter Number to check prime or Not ?"))
x=ChkPrime(iNo)
if(x==1):
    print("Not Prime Number")
else:
    print(" Prime Number")