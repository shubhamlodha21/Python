#Search the position of substring in main string

iNo=int(input("Enter number of String?"))
str=[]

print("Enter {} Strings:".format(iNo))
for i in range(iNo):
    str.append(input())

s=input("Enter Substring to search:")

ij=0
for i in range(len(str)):
    if(s==str[i]):
        ij=1
        print("Found at: {} Position".format(i))

if(ij==0):
    print("Substring Not Found !!!")