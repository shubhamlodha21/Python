#Function Name:Student
#Input:10 20 30 40 50 

#Output:Enter Marks 10 20 30 40 50
#Summation of MArks is 150
#Percentage is 30.0 %

#Description:Accept Marks from student return its Summation and Percentage
#Date: 14/07/2021
#Author: Shubham Lodha


str=input("Enter Marks").split(" ")
marks=[int(num)for num in str]

sum=0
for i in marks:
	sum=sum+i
print("Summation of MArks is",sum)

n=len(marks)
per=sum/n
print("Percentage is",per,"%")