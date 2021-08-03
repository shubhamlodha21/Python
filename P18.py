#Function Name:Display
#Input:5
#Output:1 2 3 4 5
#Description:Enter Number from user and display Number upto that Number
#Date: 03/08/2021
#Author: Shubham Lodha

def Display(no1):
    i=0
    for i in range(no1):
       print("*",end=" ")
    

def main():
  no1=int(input("Enter a Number"))
  Display(no1)
    
if __name__=="__main__":
    main()
