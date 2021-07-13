#Function Name:PosSubString
#Input:Shubham am
#Output:Sub String Found at Position 6
#Description:Find the SubString Position 
#Date: 13/07/2021
#Author: Shubham Lodha

main=input("Enter a Main String:")
sub=input("Enter a SubString:")

n=main.find(sub,0,len(main))

if n==-1:
	print("String DOesnt find")
else:
	print("Sub String Found at Position",n+1)
