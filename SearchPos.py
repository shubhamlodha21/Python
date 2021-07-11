#Function Name:SearchPos
#Input:3(Nager Rahuri Pune)  Pune
#Output:Pune Found at  position 3
#Description:Enter Cities Name and Find their Position
#Date: 12/07/2021
#Author: Shubham Lodha


str=[]
print("Enter Number of Cities")
num=int(input())

flag=False
for i in range (num):
	print("Enter Cities:",end=" ")
	str.append(input())

s=input("Enter City you want Search:")

for i in range(len(str)):
	if s==str[i]:
		print(s,"found at Position:",i+1)
		flag=True

if flag==False:
	print("Not Found..!")