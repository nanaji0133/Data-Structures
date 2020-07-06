from Stack import Stack
from Queue import Queue

class Node(object):
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class binarytree(object):
    def __init__(self,root):
        self.root = Node(root)

    def print_tree(self,traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(self.root, " ")
        elif traversal_type == "inorder":
            return self.preorder_print(self.root, " ")
        elif traversal_type == "postorder":
            return self.preorder_print(self.root, " ")
        elif traversal_type == "levelorder":
            return self.preorder_print(self,self.root)
        else:
            return False
            
    def preorder_print(self,start,traversal): # root-->left-->right
        if start:
            traversal += (str(start.data) + "-")
            traversal = self.preorder_print(start.left,traversal)
            traversal = self.preorder_print(start.right,traversal)
        return traversal

    def inorder_print(self,start,traversal): 
        if start:
            traversal = self.preorder_print(start.left,traversal)
            traversal += (str(start.data) + "-") # print(str(start.data)) no need of traversal
            traversal = self.preorder_print(start.right,traversal)
        return traversal

    def postorder_print(self,start,traversal): # root-->left-->right
        if start:
            traversal = self.preorder_print(start.left,traversal)
            traversal = self.preorder_print(start.right,traversal)
            traversal += (str(start.data) + "-")
        return traversal

    def levelorder_print(self,start): # same level
        if start is None:
            return
        q = Queue()
        q.enqueue(self.root)
        order = ""
        while q:
            order += str(q.peek()) + "-"
            node = q.dequeue()
            if node.left:
                q.enqueue(node.left)
            if node.right:
                q.enqueue(node.right)
        return order

    def size_iterative(self):
        if self.root is None:
            return 0
        s = Stack()
        s.push(self.root)
        size = 1
        while s:
            node = s.pop()
            if node.left:
                s.push(node.left)
                size += 1
            if node.right:
                s.push(node.right)
                size += 1
        return size

    def size_(self,node):
        if node is None:
            return 0
        return self.size_(node.left) + self.size_(node.right) + 1

    # def checkbst(self):
    #     return self.check_bst(self.root)

    # def check_bst(self,start): # root-->left-->right
    #     if start:
    #         self.check_bst(start.left)
    #         print(str(start.data)) # print(str(start.data)) no need of traversal
    #         self.check_bst(start.right)

    def checkbst(self):
        if self.root:
            is_satisfied = self.check_bst(self.root)
            if is_satisfied is None:
                return True
            return False
        return True


    def check_bst(self,node):
        if node is None or (node.left is None and node.right is None):
            return True
        if node.right is not None:
            if node.right.data > node.data:
               return self.check_bst(node.right)
            else:
                return False
        if node.left is not None:
            if node.left.data < node.data:
                return self.check_bst(node.left)
            else:
                return False 
        # return check_bst(node.left) and check_bst(node.right)
        
# vertical order traversal
def getvertical(m,hd,current):
        
    if current is None:
        return
        
    try:
        m[hd].append(current.data)
    except:
        m[hd] = [current.data]

    getvertical(m,hd-1,current.left)
    getvertical(m,hd+1,current.right)

def printvertical():
        
    m = dict()
    hd = 0

    getvertical(m,hd,tree.root)

    for index,key in enumerate(sorted(m)):
        for i in m[key]:
            print(i) 
        print




tree = binarytree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
printvertical()
# print(tree.checkbst())
print(tree.levelorder_print("inorder"))
# print(tree.size_iterative())
# print(tree.size_(tree.root))