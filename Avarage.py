#Find the avarage and percentage of all students

iNo=int(input("Enter number of Students:"))
lst=[]
print("Enter Marks:")
for i in range (iNo):
    ele=int(input())
    lst.append(ele)

#Summation
sum=0
for i in range (0,iNo):
    sum=sum+lst[i]
print("Summation is:",sum)

#Percentage
per=sum/iNo
print("Percentage is:",per)
