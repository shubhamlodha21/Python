#Function Name:Sort
#Input:Shubham am am (am)

#Output:Found at Position 6
#       Fount at Position 9
#       Found at Position 12

#Description:Enter String and substring found position of substring in Main String
#Date: 12/07/2021
#Author: Shubham Lodha




main=input("Enter a Main String:")
sub=input("Enter a SubString:")

pos=-1
flag=False
n=len(main)
while True:
	pos=main.find(sub,pos+1,n)
	if pos==-1:
		break

	print("Found at Position:",pos+1)
	flag=True

if flag==False:
	print("Sub String Not Found at Position")