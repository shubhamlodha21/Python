#Variable Length 
def add(farg,*args):
    print("Value at First Argument:",farg)
    print("Value at Argumenst:",args)
    sum=0
    for i in args:
        sum+=i
    print("Sum of all arguments is:",(farg+sum))
 
add(5,10)
add(55,4.6,9.2,4,5)