# Accept n numbers and display in between that range
def nPrime(iNo):
    for i in range(2,iNo+1):
        x=ChkPrime(i)
        if(x==0):
            print(i)

def ChkPrime(n):
    for i in range(2,n):
        if(n%i==0):
            return 1
    return 0

z=int(input("Enter number Upto Which you want prime series:"))
nPrime(z)