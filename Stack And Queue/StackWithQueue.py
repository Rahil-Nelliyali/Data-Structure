from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, data):
        self.items.append(data)

    def is_empty(self):
        return len(self.items) == 0

    def dequeue(self):
        if self.is_empty():
            return "Underflow"
        return self.items.popleft()

    def front(self):
        if self.is_empty():
            return "Underflow"
        return self.items[0]

    def rear(self):
        if self.is_empty():
            return "Underflow"
        return self.items[-1]

    def size(self):
        return len(self.items)

    def display(self):
        print(list(self.items))


class MyStack:
    def __init__(self):
        self.items = Queue()

    def push(self, x):
        self.items.enqueue(x)

    def pop(self):
        i = self.items.size()
        while i > 1:
            self.items.enqueue(self.items.dequeue())
            i -= 1
        return self.items.dequeue()

    def top(self):
        return self.items.rear()

    def empty(self):
        return self.items.is_empty()

    def display(self):
        return self.items.display()


obj = MyStack()
obj.push('x')
obj.push('y')

obj.pop()
obj.display()

