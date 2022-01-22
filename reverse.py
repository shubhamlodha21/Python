# Accept a String from user and display in reverse order

str=input("Enter a String:")
for ch in range(len(str)-1,-1,-1):
    print(str[ch],end="")