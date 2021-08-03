#Function Name:Table
#Input:10
#Output:2  4  6  8  
#Description:Enter Number from user and display even  Number upto that Number
#Date: 03/08/2021
#Author: Shubham Lodha

def Table(no1):
    for i in range(2,no1+1,2):
       print(i,end=" ")
    

def main():
  no1=int(input("Enter a Number"))
  Table(no1)
    
if __name__=="__main__":
    main()
