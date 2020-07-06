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

# using recursive way  
'''code is unfinished has some error'''
    def insertatRec(self,newnode,position):
        currentnode = self.head
        currentposition = 0
        if currentposition == position:
            previousnode.next = newnode
            newnode.next = currentnode
            brreak
        previousnode = currentnode
        currentnode = currentnode.next 
        currentposition += 1
        return insertatRec(self,newnode,position) 



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


    def delnodeat(self,position):
        currentnode = self.head
        currentposition = 0
        while True:
            if currentposition == position:
                previousnode.next = currentnode.next
                currentnode.next = None   
                break
            previousnode = currentnode
            currentnode = currentnode.next
            currentposition += 1

# writing a program to del the last node
    def delnode(self):
        currentnode = self.head
        
        while currentnode.next is not None:
            previousnode = currentnode
            currentnode = currentnode.next
        previousnode.next = None
        

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
# reversing the list using iterative way
    def reverse_iteratively(self):
        previousnode = None
        currentnode = self.head
        while currentnode is not None: # try for while currentnode.next is not None: case in some way
            nextnode = currentnode.next
            currentnode.next = previousnode
            previousnode = currentnode
            currentnode = nextnode
        self.head = previousnode

#reversing the list using recurssive way
    def reverse_recursive(self):
        def _reverse_recursive(currentnode, previousnode):
            if currentnode is None:
                return previousnode
            nextnode = currentnode.next
            currentnode.next = previousnode
            previousnode = currentnode
            currentnode = nextnode
            return _reverse_recursive(currentnode, previousnode)
        self.head = _reverse_recursive(currentnode= self.head, previousnode = None)





firstnode = Node("john")
linkedlist = LinkedList()
linkedlist.insertEnd(firstnode)
secondnode = Node("king")
linkedlist.insertEnd(secondnode)
midlenode = Node("raj")
linkedlist.insertEnd(midlenode)
lstnode = Node("dico")
linkedlist.insertatRec(lstnode,1)
# linkedlist.reverse_recursive()
linkedlist.printlist()


#https://github.com/vprusso/youtube_tutorials/blob/master/data_structures/linked_list/singularly_linked_list/linked_list_reverse.py



'''Print elements of a linked list in forward order using recursion '''