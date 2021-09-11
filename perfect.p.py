def perfect(l,u):
     for num in range(l,u):
          sum=0
          for i in range(1,num):
               if(num%i)==0:
                    sum=sum+i
          if(sum==num):
               print("perfect number ",sum)
l=int(input("lower bound:"))
u=int(input("upper bound:"))
perfect(l,u)
