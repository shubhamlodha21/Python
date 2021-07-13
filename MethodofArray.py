#Function Name:MethodofArray
#Input:

#Output:
#Original Array is: array('i', [10, 20, 30, 40, 50])
#After Appending 60 array('i', [10, 20, 30, 40, 50, 60])
#After Inserting 99 at position 1 array('i', [10, 99, 20, 30, 40, 50, 60])
#After removing 30 array('i', [10, 99, 20, 40, 50, 60])
#Popped Element is  60
#First Index of 40 is 4
#Array are array('i', [10, 99, 20, 40, 50])
#Converting Array into a List [10, 99, 20, 40, 50]

#Description:Methods Related to Array
#Date: 14/07/2021
#Author: Shubham Lodha




from array import *;
arr=array('i',[10,20,30,40,50])
print("Original Array is:",arr)

arr.append(60)
print("After Appending 60",arr)

arr.insert(1,99)
print("After Inserting 99 at position 1",arr)

arr.remove(30)
print("After removing 30",arr)

n=arr.pop()
print("Popped Element is ",n)

n=arr.index(40)
print("First Index of 40 is",n+1)

lst=arr.tolist()
print("Array are",arr)
print("Converting Array into a List",lst)