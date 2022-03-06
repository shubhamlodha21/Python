#Find the factorial of n numbers
def factorial(n):
    prod=1
    while n>=1:
        prod*=n
        n-=1
    return prod

iNo=int(input("Enter How many Numbers you want:"))
for i in range(1,iNo+1):
    x=factorial(i)
    print(x)