#Accept a String From user and count number of times each letter is presesnt

s=str(input("Enter a String:"))
dict={}
for x in s:
    dict[x]=dict.get(x,0) +1 

for k,v in dict.items():
    print("Key={}\t Its Occurance={}".format(k,v))