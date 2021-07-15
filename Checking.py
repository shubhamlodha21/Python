#Function Name:Checking
#Input:Shubham Lodha  (bham)
#Output:bham is Found is Main String
#Description:Check the substring is found or ot in main string
#Date: 15/07/2021
#Author:Shubham Lodha

main=input("Enter a Main String:")
sub=input("Enter a SubString:")

if sub in main:
	print(sub+"is Found is Main String")
else:
	print(sub+"is Not Found in Main String")
