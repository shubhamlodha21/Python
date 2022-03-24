#Generators 


def Mygen(x,y):
    while (x!=y):
        yield x
        x+=1

g=Mygen(10,20)
for i in g:
    print(i,end=" ")