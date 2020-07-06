class Queue:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.rear = None

    def enqueue(self,newnode):
        if self.rear is None:
            self.rear = self.head = newnode
        else:
            self.rear.next = newnode
            self.rear = self.rear.next

    def dequeue(self):
        if self.head is None:
            return "queue is empty"
        else:
            to_return = self.head.data
            self.head = self.head.next
            return to_return

    def IsEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def top(self):
        return self.head.data

    def last(self):
        return self.rear.data

    def lenqueue(self):
        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next   
        return count

    def get_Queue(self):
        if self.head is None:
            print("empty")
            return
        currentnode = self.head
        while True:
            if currentnode is None:
                break
            print(currentnode.data,end = " ")
            currentnode = currentnode.next


l = LinkedList()
l.enqueue(Queue("1"))
l.enqueue(Queue("2"))
l.enqueue(Queue("3"))
l.enqueue(Queue("4"))
l.get_Queue()
l.dequeue()
print("\n")
l.get_Queue()
print("\n")
print(l.last())
print(l.top())
print("\n")
print(l.lenqueue())
# print(l.IsEmpty)
    

