#Function Name:AnyAll
#Input: 

#Output:Result of arr>brr is [ True  True False False]
#Check if one of Condition is True: True
#Check if all of Condition is True: False 

#Description:Implementations of AnyAll
#Date: 18/07/2021
#Author: Shubham Lodha


from numpy import *

arr=array([10,20,50,60])
brr=array([30,40,50,10])

c=arr<brr
print("Result of arr>brr is",c)

print("Check if one of Condition is True:",any(c))
print("Check if all of Condition is True:",all(c))
