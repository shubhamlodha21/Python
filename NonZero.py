#Function Name:PosSubString
#Input:
#Output:[0 1 4]
#Description:Enter Position of Non-zero Values.
#Date: 13/07/2021
#Author: Shubham Lodha

from numpy import *

arr=array([10,205,0,0,50,0])

c=nonzero(arr) #INdex of non-zero elements

for i in c:
	print(i)
