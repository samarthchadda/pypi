class person:
    def __init__(self,personName,personAge):
        self.name=personName
        self.age=personAge

    def showName(self):
        print(self.name)

    def showAge(self):
        print(self.age)


class student:
    def __init__(self,Id):
        self.studentId=Id
    def getId(self):
        return self.studentId

class resident(person,student):
    def __init__(self,name,age,Id):
        person.__init__(self,name,age)
        student.__init__(self,Id)


#create an object of subclass
r1=resident('manu',30,102)
r1.showName()
print(r1.getId())
