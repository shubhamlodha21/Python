#Function Name:Search
#Input:40

#Output:
#Element Found..!

#Description:Enter number from user and check that number is present or not in given array
#Date: 17/07/2021
#Author: Shubham Lodha


list=[10,20,30,40,50]
x=int(input("Enter the Number You want to Search in list"))
for n in list:
	if x==n:
		print("Element Found..!")
		break
else:
	print("Element not Found..!")