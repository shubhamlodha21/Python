#Function Name:Reverse
#Input:Shubham
#Output:mahbuhS
#Description:Accept String from user and display it reverse
#Date: 15/07/2021
#Author:Shubham Lodha


print("Enter String:")
s=str(input())

l=len(s)
i=-1
while i>=-l:
	print(s[i],end="")
	i=i-1