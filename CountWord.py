#Function Name:CountWord
#Input:Shubhamamaa  Lodha GK Rahuri
#Output:4
#Description:Enter String and Count number of Words
#Date: 12/07/2021
#Author: Shubham Lodha

str=input("Enter a String..?")
i=c=0
flag=True
for s in str:
	if flag==False and str[i]==" ":
		c=c+1
	else:
		flag=False
	i=i+1

print("Number of Words are:",c)