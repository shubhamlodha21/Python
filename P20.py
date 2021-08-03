#Function Name:Length
#Input:Shubham
#Output:7
#Description:Enter String  from user and return length of it
#Date: 03/08/2021
#Author: Shubham Lodha


def Length(no1):
    n=len(no1)
    print("Size is",n)
    
def main():
  no1=str(input("Enter a String"))
  Length(no1)
    
if __name__=="__main__":
    main()
