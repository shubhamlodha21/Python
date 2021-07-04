
#Function Name:Commandline
#Input:--

#Output:Number of Command line args= 3
#Args are ['Commandline.py', '10', '20']

#Description:Implementations of Command Line Arguments
#Date: 04/07/2021
#Author: Shubham Lodha


#python Commandline.py 10 20

import sys
n=len(sys.argv)
argv=sys.argv
print("Number of Command line args=",n)
print("Args are",argv)