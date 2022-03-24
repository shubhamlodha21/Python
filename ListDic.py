#Converting List into Dictonaries

s=["Maharashtra","New-Delhi","Gujrat"]
c=["Mumbai","Delhi","GandhiNager"]

z=zip(s,c)
d=dict(z)

for k in d:
    print("{}-->{}".format(k,d[k]))