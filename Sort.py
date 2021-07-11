#Function Name:Sort
#Input:3(Nager Rahuri Pune)

#Output:Enter Cities:
        #Nager
        #Pune
        #Rahuri

#Description:Enter Cities Name and Sorted them according to ascending order
#Date: 12/07/2021
#Author: Shubham Lodha


str=[]
print("Enter Number of Cities")
num=int(input())

for i in range (num):
	print("Enter Cities:",end=" ")
	str.append(input())

str1=sorted(str)
print("Sorted Cities is:")
for i in  str1:
	print(i)