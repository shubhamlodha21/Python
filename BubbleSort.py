#Bubble_Sort

from array import *
x=array('i',[])
iNo=int(input("Enter number of Elements you want:"))

print("Enter Elements:")
for i in range(iNo):
    x.append(int(input()))

for i in range (iNo-1):
    for j in range (0,(iNo-1-i)):
        if x[j]>x[j+1]:
            temp=x[j]
            x[j]=x[j+1]
            x[j+1]=temp

print("Sorted List is:")
for i in range (iNo):
    print(x[i],end=" ")