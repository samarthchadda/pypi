class student:
    def getStudent(self):
        self.name=input("Name:")
        self.age=input("Age:")
      

class test(student):
    def getmarks(self):
        print("Enter marks of respective subjects")
        self.phy=int(input("Physics:"))
        self.math=int(input("Maths:"))
        self.chem=int(input("Chemistry:"))

class marks(test):
    def display(self):
        print("\nName:",self.name)
        print("Age:",self.age)
        print("Total Marks:",self.phy+self.math+self.chem)

m1=marks()
m1.getStudent()
m1.getmarks()
m1.display()

        
