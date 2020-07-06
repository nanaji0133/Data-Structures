# creating linkedlist and adding new head node at the begining
class Node:
    def __init__(self,data): #creating node
        self.data = data
        self.next = None
class LinkedList: # creating linkedlist
    def __init__(self):
        self.head = None # created empty list
    
    def insertHead(self,newnode): # creating new head to our lnkdlist and changing our previous head
        tmproryNode = self.head #saving the current node in the temporary place for not to loosse the connection
        self.head = newnode  # our new head
        self.head.next = tmproryNode
        del tmproryNode

    def insertEnd(self,newnode):
        if self.head is None:
            self.head = newnode
        else:
            lastnode = self.head # creating traversal
            while True:
                if lastnode.next is None: # intially only one data 1st node
                    break
                lastnode = lastnode.next 
            lastnode.next = newnode # assigning lastnode.next value
    def printlist(self):
        if self.head is None:
            print("empty")
            return
        currentnode = self.head
        while True:
            if currentnode is None:
                break
            print(currentnode.data)
            currentnode = currentnode.next



firstnode = Node("john")
linkedlist = LinkedList()
linkedlist.insertEnd(firstnode)
secondnode = Node("king")
linkedlist.insertEnd(secondnode)
newHead = Node("raj")
linkedlist.insertHead(newHead)
linkedlist.printlist()