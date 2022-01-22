#Display Prime Numbers upto n 

n=int(input("Enter Numbers Upto which you want prime series ?"))

def isPrime(i):
    for j in range (2,i):
        if(i%j==0):
            return 1
    return 0

for i in range(2,n):
    bRet=isPrime(i)
    if(bRet==0):
        print(i,end=" ")
    
