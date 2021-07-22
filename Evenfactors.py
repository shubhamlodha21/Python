#Function Name:EvenFactors
#Discription: Even factor program
#Input:10
#Output:2 10
#Date: 22/07/2021
#Author:Shubham Lodha
x = int(input("Enter any number"))
print("The even factors of",x,"are:")
for i in range(2, x + 2):
    if x % i == 0:
            print(i)