names = "Shubham, Grandy, Dev"
length = len(names)

print(length)

print(names)
#Positive Slicing
print("Print Using Slice Operation:" + names[0:20:1])

#Negative Slicing
# Internally -> (+names[0:len(names)-10:1])
#               (names[0:10:1])

print("Print Using Slice Operation:" + names[0:-10:1])

# names[11:15]
print("Print Using Slice Operation:" + names[-9:15:1])
