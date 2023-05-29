class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class Stack:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("Queue is empty")
        else:
            n = self.head
            while n:
                print(n.data)
                n = n.ref

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.ref = self.head
            self.head = new_node

    def pop(self):
        self.head = self.head.ref

    def peek(self):
        print(self.head.data)


s = Stack()
s.push(12)
s.push(14)
s.push(19)
s.pop()
s.display()
