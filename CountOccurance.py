#Count Occarance

x=[]
n=int(input("Enter Number of Elements you want:"))
for i in range (n):
    x.append(input("Enter Elements==>"))


z=0
y=int(input("Enter the Element whose count you want:"))
for i in x:
    if(y==i):
        z+=1
    #print(z)
print("Count of %d is %d times"%(y,z))


