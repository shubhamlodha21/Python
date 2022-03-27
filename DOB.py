#Class within another class (inner class) Concept Data-of-Birth

class Person:
    def __init__(self):
        self.name="Shubham"
        #self.db=self.Dob()

    def Display(self):
        print("Name is-",self.name)

    class DOB:
        def __init__(self):
            self.dd=21
            self.mm=11
            self.yy=2001
        
        def Display(self):
            print("DOB is {}/{}/{}".format(self.dd,self.mm,self.yy))

P=Person()
P.Display()
X=Person().DOB()
X.Display()
