
class Queue(object):
    def __init__(self):
        self.list = []
    
    def IsEmpty(self):
        return self.list == []

    def enqueue(self,item):
        self.list.insert(0,item)

    def dequeue(self):
        self.list.pop()

    def peek(self):
        return self.list[-1]

    def printlist(self):
        return self.list
        # for char in self.list:
        #     print(char, end = " ")

# q = Queue()
# q.enqueue("1")
# q.enqueue("2")
# q.enqueue("3")
# print(q.printlist())
# q.dequeue()
# print(q.printlist())