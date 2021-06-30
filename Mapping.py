#Function Name:Mapping
#Input:--

#Output:{10: 'Shubham', 11: 'Shiva', 12: 'Hrutik', 13: 'Bhavna', 14: 'Prasad'}
#Values of Keys dict_keys([10, 11, 12, 13, 14])
#Values tobe Stored dict_values(['Shubham', 'Shiva', 'Hrutik', 'Bhavna', 'Prasad'])
#After Updation {10: 'Shubham', 11: 'Shiva', 12: 'Hrutik', 13: 'Bhavna', 14: 'Shub'}
#After Deleting {10: 'Shubham', 11: 'Shiva', 12: 'Hrutik', 13: 'Bhavna'}

#Description:Implementation of Mapping
#Date: 30/06/2021
#Author: Shubham Lodha

d={10:"Shubham",11:"Shiva",12:"Hrutik",13:"Bhavna",14:"Prasad"}
print(d)
print("Values of Keys",d.keys())
print("Values tobe Stored",d.values())
d[14]="Shub"
print("After Updation",d)
del d[14]
print("After Deleting",d)