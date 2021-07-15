#Function Name:Prime
#Input: 17
#Output:17 is Prime Number
#Description:Accept Number from user and check number is Prime
#Date: 16/07/2021
#Author:Shubham Lodha


def Prime(n):
	x=1
	for i in range(2,n):
		if n%i==0:
			x=0
			break
		else:
			x=1
	return x

num=int(input("Enter a Number"))
result=Prime(num)
if result==1:
	print(num,"is Prime Number")
else:
	print(num,"is Not Prime Number")