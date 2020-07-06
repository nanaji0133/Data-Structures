# from Stack import Stack
# from Queue import Queue

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self,newvalue):
        if self.root is None:
            self.root = Node(newvalue)
        else:
            self._insert(newvalue,self.root)

    def _insert(self,newvalue,currentvalue):
        if (newvalue > currentvalue.data):
            if currentvalue.right is None:
                currentvalue.right = Node(newvalue)
            else:
                self._insert(newvalue,currentvalue.right)

        elif (newvalue < currentvalue.data):
            if currentvalue.left is None:
                currentvalue.left = Node(newvalue)
            else:
                self._insert(newvalue,currentvalue.left)

    # def search(self, find_val):
    #     return self.search_helper(self.root, find_val)

    # def search_helper(self, current, find_val):
    #     if current:
    #         if current.data == find_val:
    #             return True
    #         elif current.data < find_val:
    #             return self.search_helper(current.right, find_val)
    #         else:
    #             return self.search_helper(current.left, find_val)

    def find(self,value):
        return self._find(value,self.root)

    def _find(self,value,currentvalue):
        if currentvalue:
            if value == currentvalue.data:
                return True
            elif value < currentvalue.data:
                return self._find(value,currentvalue.left)   
            elif value > currentvalue.data:   
                return self._find(value,currentvalue.right)
        else:
            return False

    def delete(self,newvalue):
        if self.root is None:
            self.root = Node(newvalue)
        else:
            self._insert(newvalue,self.root)

    def _insert(self,newvalue,currentvalue):
        if (newvalue > currentvalue.data):
            if currentvalue.right is None:
                currentvalue.right = Node(newvalue)
            else:
                self._insert(newvalue,currentvalue.right)

        elif (newvalue < currentvalue.data):
            if currentvalue.left is None:
                currentvalue.left = Node(newvalue)
            else:
                self._insert(newvalue,currentvalue.left)

    def min(self):
        return self._min(self.root)

    def _min(self,current):
        if current.left is None:
            return current.data
        else:
            return self._min(current.left)

    def min_iterative(self):
        current = self.root
        while True:
            if current.left is not None:
                current = current.left
            else:
                return current.data

    def max(self):
        return self._max(self.root)

    def _max(self,current):
        if current.right is None:
            return current.data
        else:
            return self._max(current.right)
            
    def height(self,node):
        if node is None:
            return -1
        return (max(self.height(node.left), self.height(node.right)) + 1)

    def size(self):
        if self.root is None:
            return 0
        s = Stack()
        s.push(self.root)
        size = 1
        while s is not None:
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

    def checkbst(self):
        return self.check_bst(self.root)


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

    def inorder_succesor(self,current):
        current = self.find(current)
        if current is None:
            return None
        if Node(current).right:
            return self.min()
        else:
            succesor = None
            ancestor = self.root
            while ancestor != current:
                if Node(current).data < ancestor.data: '''AttributeError: 'NoneType' object has no attribute 'data''''
                    succesor = ancestor
                    ancestor = ancestor.left
                else:
                    ancestor = ancestor.right
            else:
                return succesor


b = BST()
b.insert(10)
b.insert(2)
b.insert(5)
b.insert(6)
b.insert(3)

print(b.inorder_succesor(2))
# print(b.checkbst())
# print(b.find(22))
# print(b.min_iterative())
# print(b.max())
# print(b.height(b.root))
# print(b.size_(b.root))