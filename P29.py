#Function Name:NumberofDigit
#Input:123654
#Output:6
#Description:Accept number from user and return number of its Digits
#Date: 05/08/2021
#Author: Shubham Lodha

def NumberofDigit(ino):
    count=0
    while ino!=0:
        ino=ino//10
        count=count+1
    print("Number of Digits are:",str(count))
    
def main():
    ino=int(input("Enter a Number"))
    NumberofDigit(ino)

if __name__=="__main__":
    main()

 

