#Function Name:SumEven
#Input:10 20 30 40 
#Output:Sum of Even Numbers is 100
#Description:Sum of all Even Numbers using Command-Line Arguments
#Date: 08/07/2021
#Author: Shubham Lodha

#python SumEven.py 10 20 30 40 

import sys
 
args=sys.argv[1:]
print(args)

sum=0
for a in args:
	x=int(a)
	if x%2==0:
		sum=sum+x

print("Sum of Even Number is ",sum)