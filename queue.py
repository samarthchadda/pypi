class Queue:
    def __init__(self):
        self.queue=[]    #empty array

    def isEmpty(self):
        return self.queue==[]

    def enqueue(self,data):
        self.queue.append(data)

    def dequeue(self):
        data=self.queue[0]       #first item of queue
        del self.queue[0]
        return data

    def peek(self):
        return self.queue[0]

    def sizeQueue(self):
        return len(self.queue)

q=Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(70)

print(q.sizeQueue())

print("Dequeue:",q.dequeue())

print("Dequeue:",q.dequeue())

print(q.sizeQueue())
