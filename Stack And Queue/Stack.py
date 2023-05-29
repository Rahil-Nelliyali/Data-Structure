class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def print_items(self):
        if self.is_empty():
            print("Stack is empty. Nothing to print.")
        else:
            print(self.items)

    def middle_element_delete(self):
        mid = len(self.items) // 2
        temp_stack = Stack()

        for i in range(mid):
            temp_stack.push(self.pop())
        self.pop()

        while not temp_stack.is_empty():
            self.push(temp_stack.pop())

    def find_middle(self):
        stack_length = len(self.items)
        mid_index = stack_length // 2

        if stack_length % 2 == 0:
            mid_index -= 1

        return self.items[mid_index]

    def top(self):
        if self.is_empty():
            print("Stack is empty!")

        else:
            print(self.items[0])

    def second_largest(self):
        if self.is_empty():
            print("stack is empty")
        else:
            largest = float('-inf')
            second_largest = float('-inf')

            for element in self.items:
                if element > largest:
                    second_largest = largest
                    largest = element
                elif element > second_largest:
                    second_largest = element

            return second_largest

    def add_at_middle(self, x):
        if self.is_empty():
            print("stack is empty")
        else:
            aux_stack = []
            mid = len(self.items) // 2

            for i in range(mid):
                aux_stack.append(self.pop())
            aux_stack.append(x)

            while aux_stack:
                self.items.append(aux_stack.pop())

    def add_at_position(self, x, pos):
        if self.is_empty():
            print("stack is empty")
        else:
            aux_stack = []

            while len(self.items) > pos - 1:
                aux_stack.append(self.pop())
            aux_stack.append(x)

            while aux_stack:
                self.items.append(aux_stack.pop())

    def update_value(self, x, value):
        if self.is_empty():
            print("stack is empty")
        else:
            found = False
            aux_stack = []
            while self.items:
                element = self.pop()
                if element == value:
                    element = x
                    found = True
                aux_stack.append(element)
            if not found:
                print("Item not found")
            while aux_stack:
                self.items.append(aux_stack.pop())


def reverse_string(input_str):
    stack = Stack()

    # Push each character onto the stack
    for i in input_str:
        stack.push(i)

    reversed_str = ""

    # Pop each character from the stack and append it to the reversed string
    while not stack.is_empty():
        reversed_str += stack.pop()

    return reversed_str


# Example usage
input_string = "Hello, World!"
reversed_string = reverse_string(input_string)
print(reversed_string)  # Output: !drollW ,olleH

new_stack = Stack()
new_stack.push(45)
new_stack.push(56)
new_stack.push(88)

new_stack.print_items()
second_big = new_stack.second_largest()
print("Second largest : ", second_big)
new_stack.add_at_middle(5)
new_stack.add_at_middle(67)
new_stack.add_at_position(4, 4)
new_stack.print_items()
new_stack.update_value(100, 56)
new_stack.print_items()
