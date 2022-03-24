#Tower of Hanoi

def Towers(n,a,c,b):
    if(n==1):
        print("Move Disk %i from pole %s to pole %s" %(n,a,c))
    else:
        Towers(n-1,a,b,c)
        print("Move disk %i from pole %s to pole %s" %(n,a,c))
        Towers(n-1,b,c,a)

n=int(input("Enter number of Disks:"))
Towers(n,"A","C","B")