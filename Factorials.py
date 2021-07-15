#Function Name:Factorials
#Input: 
#Output:1 2 6 24 120
#Description:Factorial of First 5 Numbers
#Date: 16/07/2021
#Author:Shubham Lodha


def Factorial(n):
	prod=1
	while n>=1:
		prod=prod*n
		n=n-1
	return prod

for i in range(1,5):
	print("Factorial of {} is {}".format(i,Factorial(i)))