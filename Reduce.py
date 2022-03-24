# Use of reduce function

from functools import reduce

sum=reduce(lambda a,b:a+b,range(1,51))
print("Sum of First 50 numbers is:",sum)
