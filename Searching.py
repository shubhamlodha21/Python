#Function Name:Searching
#Input:5(10 20 30 40 50)   20 
#Output:Found at position 2
#Description:Enter the Elements and Found it Position
#Date: 10/07/2021
#Author: Shubham Lodha



from array import *
x=array('i',[])
print("How Many Elements..?",end='')
n=int(input())

for i in range (n):
    print("Enter Elements:",end=" ")
    x.append(int(input()))
print("Array List  is:",x)

print("Enter Elements to Search:",end=" ")
s=int(input())

try:
	pos=x.index(s)
	print("Found at Position",pos+1)
	#break

except ValueError:
	print("Elements Not Found in Array..!")