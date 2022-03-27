#Class and Objects BAsic OOPS 

class Student:
    def __init__(self):
        self.name="SHUBHAM"
        self.age=20
        self.marks=94

    def talk(self):
        print("Hii, I am",self.name)
        print("My age is",self.age)
        
        print("My Marks are:",self.marks)

s1=Student()
s1.talk()

