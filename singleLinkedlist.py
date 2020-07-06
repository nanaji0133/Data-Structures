# creating linkedlist and adding new node at the end
class Node:
    def __init__(self,data): #creating node
        self.data = data
        self.next = None
class LinkedList: # creating linkedlist
    def __init__(self):
        self.head = None # created empty list

    def insert(self,newnode):
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
linkedlist.insert(firstnode)
secondnode = Node("king")
linkedlist.insert(secondnode)
thirdnode = Node("raj")
linkedlist.insert(thirdnode)
linkedlist.printlist()