class MyClass:
    a=10
    def func(self):
        print("Hello")

#create a new object
ob=MyClass()

print(MyClass.func)

print(ob.func)

ob.func()
