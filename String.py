#Strings are Immutable (NOT CHANGED)

name = "Shubham"
surname  = 'Lodha'
Address  = """ Gokul Coloney
 Rahuri """
            
print(name + " " + surname + "\n"  + Address)
print("One Word:" + name[0])

print("Print Using for-Loop:")
for i in Address:
    print(i + " ")
print("\n")