'''input:- --
output:-
1
3
5
7
9
11
13
15
17
19
description: Continue statement to print odd numbers till range
date: 28-08-2021
Author name: Shubham Lodha'''

for x in range(20):
   
    if(x%2==0):
        continue
    print(x)