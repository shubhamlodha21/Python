#Mapping with Lambda Function

list1=[5,10,15,20,25]
list2=[3,6,9,12,15]
list3=list(map(lambda x,y: x*y,list1,list2))
print("Product is=>",list3)