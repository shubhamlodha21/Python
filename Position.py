#Python Program to find position of element in array

iNo=int(input("Enter Number of Elements:"))
x=list()
print("Enter Elements:")
for i in range (iNo):
    x.append(input())

ans=int(input("Enter a Position you want find:"))
print("Element at that position is:",x[ans-1]) 
