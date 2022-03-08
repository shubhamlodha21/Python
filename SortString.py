#Enter Number of String and Sorted them in ASC Order

iNo=int(input("Enter number of Cities?"))
str=[]

print("Enter {} cities name:".format(iNo))
for i in range(iNo):
    str.append(input())

str1=sorted(str)
print(str1)