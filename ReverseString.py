#Accept the String from user and display in reverse order

st=str(input("Enter a String:"))
for i in st[::-1]:
    print(i,end="")