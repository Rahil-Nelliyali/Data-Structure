class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


class Queue:
    def __init__(self):
        self.stack = Stack()
        self.sec = Stack()

    def enqueue(self, data):
        self.stack.push(data)

    def dequeue(self):
        if not self.stack.is_empty():
            while self.stack.size() > 0:
                self.sec.push(self.stack.pop())
            popped = self.sec.pop()

            while self.sec.size() > 0:
                self.stack.push(self.sec.pop())
            return popped
        return None

    def display(self):
        print(self.stack.items)


q = Queue()
q.enqueue('a')
q.enqueue('b')
q.enqueue('c')
q.display()
q.dequeue()

q.display()
