class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def display(self):
        if self.head is None:
            print("Queue is empty")
        else:
            n = self.head
            while n:
                print(n.data)
                n = n.ref

    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.ref = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head is None:
            print("qQU is empty")
        else:
            x = self.head.data
            self.head = self.head.ref

            if self.head is None:
                self.tail = None
        return x


q = Queue()
q.enqueue(10)
q.enqueue(14)
q.enqueue(16)
q.display()
q.dequeue()
q.display()



