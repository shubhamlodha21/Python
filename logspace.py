#Function Name:logspace
#Input:
#Output:10.0 25.1 63.1 158.5 398.1 1000.0
#Description:Display Numbers from 10 to 1000 divides into 6 equals parts
#Date: 14/07/2021
#Author: Shubham Lodha

from numpy import *
a=logspace(1,3,6)
n=len(a)
for i in range (n):
	print("%.1f" %a[i],end=" ")