
#Function Name:PieGraph
#Description:Creates a PieGraph of Given Infornmations
#Date: 25/07/2021
#Author: Shubham Lodha

import matplotlib.pyplot as p
s=[40,10,30,20]
l=["Phython","C-Programming","JavaScript","HTML-CSS"]
p.pie(s,labels=l)
p.show()