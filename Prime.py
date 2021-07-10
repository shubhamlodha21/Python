#Function Name:Prime
#Input:10 20 
#Output: 11 13 17 19
#Description:Display the Prime Numbers Between the range
#Date: 10/07/2021
#Author: Shubham Lodha

lower = int(input("Enter lower range: "))  
upper = int(input("Enter upper range: "))  
  
for num in range(lower,upper + 1):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           print(num)  