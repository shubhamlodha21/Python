#Function Name:Pattern
#Input:5
#Output:
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

#Description:Print the pattern
#Date: 05/08/2021
#Author: Shubham Lodha

def Pattern(no):
    for i in range(0,no+1,1):
        for j in range(1,no+1,1):
            if(i>=j):
                print(j,end=" ")
        print("")

def main():
    no1=int(input("Enter Number"))
    Pattern(no1)

if __name__=="__main__":
    main()
