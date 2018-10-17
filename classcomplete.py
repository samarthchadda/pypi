class employee:
    empcount=0

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        employee.empcount+=1

    def displaycount(self):
        print("Total Employee:",employee.empcount)

    def displayemployee(self):
        print("Name:",self.name,",Salary:",self.salary)


emp1=employee("abc",2000)
emp2=employee("wxy",5000)

emp1.displayemployee()
emp2.displayemployee()
print("Total Employee:",employee.empcount)
