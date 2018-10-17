class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def getarea(self):
        print(self.length*self.breadth,"is area of rectangle")

class square(rectangle):
    def __init__(self,side):
        self.side=side
        rectangle.__init__(self,side,side)

    def getarea(self):
        print(self.side*self.side,"is area of square")

s=square(4)
r=rectangle(2,4)
s.getarea()
r.getarea()


