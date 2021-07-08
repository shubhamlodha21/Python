#Function Name:Array
#Input:--
#Output:Elements of Array is
        #5
        #6
        #-7
        #8
#Description:Display Elements of Arrays
#Date: 08/07/2021
#Author: Shubham Lodha

import array

arr=array.array('i',[5,6,-7,8])
print("The elements of Array is")
for x in arr:
	print(x)