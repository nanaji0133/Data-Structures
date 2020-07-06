# b/w two nodes 
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None

    def lenlist(self):
        length = 0
        currentNode = self.head
        if currentNode is not None:
            length += 1
            currentNode = currentNode.next
        return length

    def insertHead(self,newnode): # creating new head to our lnkdlist and changing our previous head
        tmproryNode = self.head #saving the current node in the temporary place for not to loosse the connection
        self.head = newnode  # our new head
        self.head.next = tmproryNode
        del tmproryNode

    def insertAt(self,newnode,position):
        if position<0 or position > self.lenlist():
            print("invalid")
            return

        if position == 0:
            self.insertHead(newnode)
            return
        currentnode = self.head
        currentposition = 0
        while True:
            if currentposition == position:
                previousnode.next = newnode
                newnode.next = currentnode
                break
            previousnode = currentnode
            currentnode = currentnode.next 
            currentposition += 1


    def insertEnd(self,newnode):
        if self.head is None:
            self.head = newnode
        else:
            lastnode = self.head
            while True:
                if lastnode.next is None:
                    break
                lastnode = lastnode.next
            lastnode.next = newnode

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
midlenode = Node("raj")
linkedlist.insertAt(midlenode,1)
linkedlist.printlist()
    