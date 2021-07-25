#Function Name:LB24
#Input:30  3
#Output:30	30	30
#Description:Accept two numbers from user and display first number in second number of times
#Date: 26/07/2021
#Author: Shubham Lodha


No1=int(input("Enter number"))
Value=int(input("Enter How Many Times Display"))

for i in range(1,Value+1,1):
	print(No1,end=" ")