#Function Name:MaxMinArray
#Input: 5 (10 50 90 -5 0)

#Output:Maximum Element is 90
#       Minimum Element is -5

#Description:Find MAximum and Minimum of matrix 
#Date: 11/07/2021
#Author: Shubham Lodha


from numpy import *

arr=[]
print("ENter Number of Elements")
n=int(input())

for i in range (n):
	print("Enter Elements")
	no=int(input())
	arr.append(no)

print("Maximum Element is",max(arr))
print("Minimum Element is",min(arr))
print("Mean is",mean(arr))