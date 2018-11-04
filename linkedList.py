class Node(object):
    def __init__(self,data):      #init constructor
        self.data=data;             #creating data variables
        self.NextNode=None;      #reference for next node


class linkedList(object):
    def __init__(self):
        self.head=None;      #head i.e first node of linked list
        self.size=0;

    def insertStart(self,data):         
                                        
        self.size=self.size+1      #incrementing the size of linked list

        #instantiating a class
        #i.e. creating object
        newNode=Node(data)

        if not self.head:               #if head is none
            self.head=newNode
        else:                           #if head or root node is already present
            newNode.NextNode=self.head      #current node is pointing to previous node( here updating the pointer)
            self.head=newNode               #now new node is the head node
            
    def size(self):
        return self.size;


    #more complex method with O(N) complexity
    def size2(self):
        actualNode=self.head
        size=0

        while actualNode is not None:
            size+=1
            actualNode=actualNode.NextNode

        return size
    



    def insertEnd(self,data):
        self.size+=1
        newNode=Node(data)
        actualNode=self.head      #storing first node of linked list

        #traversing till last node
        while actualNode.NextNode is not None:       #finding end of linked list
            actualNode=actualNode.NextNode


        #updating the pointer
        actualNode.NextNode=newNode



    #traversing the list
    def traverseList(self):
        actualNode=self.head

        while actualNode is not None:
            print(actualNode.data,end="\t")
            actualNode=actualNode.NextNode


    #removing a node
    def removeNode(self,reqdata):

        if self.head is None:       #if linked list is empty
            return

        self.size-=1
        currentNode=self.head
        previousNode=None

        while currentNode.data != reqdata:       #checking required data with data of current node
            previousNode=currentNode
            currentNode=currentNode.NextNode


        if previousNode is None:                   #it means we have to remove the root node
            self.head=currentNode.NextNode
        else:
            previousNode.NextNode=currentNode.NextNode
            
            
            
            
linkedlist=linkedList()

linkedlist.insertStart(12)
linkedlist.insertStart(122)
linkedlist.insertStart(3)
linkedlist.insertEnd(31)


linkedlist.traverseList()

# printing size of linked list
print("\n\n{}".format(linkedlist.size))


        
linkedlist.removeNode(31)



#linkedlist.traverseList()
#print("\n\n{}".format(linkedlist.size))




linkedlist.removeNode(3)



linkedlist.traverseList()
print("\n\n{}".format(linkedlist.size))



#inserting at last
linkedlist.insertEnd(20)
linkedlist.traverseList()
print("\n\n{}".format(linkedlist.size))



        
