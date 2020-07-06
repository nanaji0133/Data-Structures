class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

# insert at the end in the double linkedlist iterative way
    def insertEnd(self,newnode):
        if self.head is None:
            newnode.prev = None
            self.head = newnode
        else:
            lastnode = self.head
            while True:
                if lastnode.next is None:
                    break
                lastnode = lastnode.next
                newnode.prev = lastnode
            lastnode.next = newnode

# insert the newnode at the begining
    def insertNewHead(self,newnode):
        tmrynode = self.head
        self.head = newnode
        self.head.prev = None
        self.head.next = tmrynode

# insert the newnode in between the exsiting nodes
    def insertAt(self,newnode,position):
        currentnode = self.head
        currentposition = 0
        while True:
            if currentposition == position:
                previousnode.next = newnode
                newnode.prev = previousnode
                newnode.next = currentnode
                break
            previousnode = currentnode
            currentnode = currentnode.next
            newnode.prev = currentnode
            currentposition += 1

# del last node in double linkedlist
    def delendnode(self):
        currentnode = self.head
        while currentnode.next is not None:
            previousnode = currentnode
            currentnode = currentnode.next
            currentnode.prev = previousnode
        previousnode.next = None

#del specific node
    def delAt(self,position):
        currentnode = self.head
        currentposition = 0
        while True:
            if currentposition == position:
                previousnode.next = currentnode.next
                currentnode.next = None
                break
            previousnode = currentnode
            currentnode = currentnode.next
            currentnode.prev = previousnode
            currentposition += 1

#printing the list
    def printlist(self):
        if self.head is None:
            print("empty")
            return
        lastnode = self.head
        while True:
            if lastnode is None:
                break
            print(lastnode.data)
            # print(lastnode.next)
            # print(lastnode.prev)
            print("\n")
            lastnode = lastnode.next      

linkedlist = LinkedList()
node1 = Node(1)
linkedlist.insertEnd(node1)
node2 = Node(2)
linkedlist.insertEnd(node2)
node3 = Node(3)
linkedlist.insertEnd(node3)
node4 = Node(4)
linkedlist.insertNewHead(node4)
node5 = Node(5)
linkedlist.insertAt(node5,2)
linkedlist.delendnode()
linkedlist.delAt(2)
linkedlist.printlist()
