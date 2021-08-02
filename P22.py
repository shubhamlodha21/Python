#Function Name:Pattern
#Input:4
#Output:

#* * * * 
#* * * *
#* * * *
#* * * *

#Description:Print the Pattern
#Date: 02/08/2021
#Author: Shubham Lodha

def Pattern(no):
    for i in range(no):
        for j in range(no):
            print("*",end=" ")
        print("")

def main():
    no1=int(input("Enter Number"))
    Pattern(no1)

if __name__=="__main__":
    main()
