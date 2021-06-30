#Function Name:bytearray
#Input:--
#Output:99 22 0 40 15
#Description:Implementation of bytearray with modifications
#Date: 30/06/2021
#Author: Shubham Lodha

element=[10,20,0,40,15]
x=bytearray(element)
for i in x: print(i)
print("Modifying some elements")
x[0]=99
x[1]=22
for i in x: print(i)
