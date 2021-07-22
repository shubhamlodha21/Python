#Function Name:NestedFor
#Discription: A program to display number from 1 to 100 in 10 rows and 10 coloum using nested for loop.
#Input:--
#Output:--
#Date: 22/07/2021
#Author:Shubham Lodha

for i in range(1,11):
	for j in range(1,11):
		print(i*j,'\t',end='')
	print()