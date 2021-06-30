#Function Name:List
#Input:--

#Output:[10, 20, -85.6, 'Shubham', 'Sidd']
#Printing List 2 Times [10, 20, -85.6, 'Shubham', 'Sidd', 10, 20, -85.6, 'Shubham', 'Sidd']
#Displaying Elements From 0 to 4 [10, 20, -85.6, 'Shubham']
#Display Last Element Sidd
#[11, 20, -85.6, 'Shubham', 'Sidd']

#Description:Implementation of List with modifications
#Date: 30/06/2021
#Author: Shubham Lodha


list=[10,20,-85.6,"Shubham","Sidd"]
print(list)
print("Printing List 2 Times",list*2)
print("Displaying Elements From 0 to 4",list[0:4])
print("Display Last Element",list[-1])
list[0]=11
print(list)