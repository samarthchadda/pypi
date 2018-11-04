#Implementation using an array
class Stack:
    def __init__(self):
        self.stack=[]          #1D array

    def isEmpty(self):
        return self.stack==[]      #return boolean , true or false(true for empty)

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        data=self.stack[-1]     #last item
        del self.stack[-1]    #getting rid of last item(deleting from the memory)
        return data

    def peek(self):
        return self.stack[-1]

    def sizeStack(self):
        return len(self.stack)


stack=Stack()
stack.push(1)
stack.push(90)
stack.push(5)
stack.push(8)

print("Size of stack is:",stack.sizeStack())

print("Popped Item is:",stack.pop())

print("Popped Item is:",stack.pop())

print("Peeked Item is:",stack.peek())
print("Size of stack is:",stack.sizeStack())
