x={}

print("How many Players ?")
n=int(input())

for i in range (n):
    print("Enter Player Name:")
    k=input()
    print("Enter Runs:")
    v=int(input())
    x.update({k:v})

    print("Players Name:")
    for pname in x.keys():
        print(pname)

    print("Players Marks:")
    for pno in x.values():
        print(pno)
