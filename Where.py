#Function Name:Where
#Input:--

#Output:[10,20,0,0]

#Description:Used of where Keyword 
#Date: 11/07/2021
#Author: Shubham Lodha


from numpy import *

arr=array([10,20,50,60])
brr=array([30,40,50,10])

c=where(arr<brr,arr,0)
print(c)
