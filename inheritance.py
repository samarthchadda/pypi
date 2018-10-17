class user:
    name=""

    def __init__(self,name):
        self.name=name

    def printname(self):
        print("Name=",self.name)

class programmer(user):
    def __init__(self,name):
        self.name=name

    def dopython(self):
        print("Programming Python")


obj=user("samarth")
obj.printname()

obj1=programmer("manu")
obj1.printname()
obj1.dopython()
