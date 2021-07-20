#Function Name:LB14
#Input:55
#Output:55 is Divisible by 5
#Description: Accept one number and check whether is is divisible by 5 or not.
#Date: 21/07/2021
#Author: Shubham Lodha




iNo=int(input("Enter a Number"))
if(iNo==0):
	print(iNo," is Not Divisible by 5")
elif(iNo%5==0):
	print(iNo," is Divisible by 5")
else:
	print(iNo," is Not Divisible by 5")