#Recursive functions to calculate factorial of n numbers

def Factorial(n):
    if(n==0):
        return 1
    else:
        result=n*Factorial(n-1)
    return result

for i in range(1,11):
    print("Factorila of {} is {}".format(i,Factorial(i)))