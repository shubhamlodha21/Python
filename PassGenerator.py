#Function Name:PassGenerator
#Input:

#Output:5=qPtGUP;kaV+^a
#       Mlg`ws0.keCc3S8         

#Description:Random Password Generator 
#Date: 18/07/2021
#Author: Shubham Lodha

import string as s
from random import *
ch=s.ascii_letters+s.digits+s.punctuation

password="".join(choice(ch) for x in range (randint(8,16)))
print(password)