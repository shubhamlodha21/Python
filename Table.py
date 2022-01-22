#Display Table from 1 to 10

for i in range (1,11):
    for j in range (i,i*11,i):
        print(j,end="  ")
    print("\n")