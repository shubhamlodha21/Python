#Display Fibonacci Series upto n numbers

n=int(input("How Many Numbers you want in Series:"))
f1=0;f2=1;f3=0
print("0",end=" ")
for i in range (1,n):
    f3=f1+f2
    print(f3,end=" ")
    f1=f2
    f2=f3
    f3=f1