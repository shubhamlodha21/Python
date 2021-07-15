#Function Name:CheckNo
#Input: -5
#Output:-5 is Negative Number
#Description:Accept Number from user and return type of Number
#Date: 16/07/2021
#Author:Shubham Lodha


n=int(input("Enter a Number"))
if n==0:
	print(n,"is Zero")
elif n<0:
	print(n,"is Negative Number")
else:
	print(n,"is positive Number")