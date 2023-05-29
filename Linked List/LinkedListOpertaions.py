class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        if self.head is None:
            print("LL is empty")
        else:
            n = self.head
            while n:
                print(n.data)
                n = n.ref

    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def delete_begin(self):
        if self.head is None:
            print("LL is empty")
        else:
            self.head = self.head.ref

    def delete_end(self):
        if self.head is None:
            print("LL is empty")
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

    def delete_value(self, x):
        if self.head is None:
            print("LL is empty")
            return
        if self.head.data == x:
            self.head = self.head.ref
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            else:
                n = n.ref
        if n.ref is None:
            print("Node nto found")
        else:
            n.ref = n.ref.ref

    def add_after(self, data, x):
        new_node = Node(data)
        n = self.head
        while n:
            if n.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("Node not found")
        else:
            new_node.ref = n.ref
            n.ref = new_node

    def add_before(self, data, x):
        if self.head is None:
            print("LL is empty")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref:
            if n.ref.data == x:
                break
            n = n.ref

        if n.ref is None:
            print("Node not found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def largest_element(self):
        if self.head is None:
            print("LL is empty")
        else:
            n = self.head
            max1 = self.head.data
            while n:
                if n.data > max1:
                    max1 = n.data
                n = n.ref
            print("largest ", max1)

    def second_largest(self):
        if self.head is None:
            print("LL is empty")
        else:
            n = self.head
            max1 = self.head.data
            max2 = float('-inf')
            while n:
                if n.data > max1:
                    max2 = max1
                    max1 = n.data
                elif max1 > n.data > max2:
                    max2 = n.data
                n = n.ref
            print("second largest ", max2)

    def prime_items(self):
        if self.head is None:
            print("LL is empty")
        else:
            n = self.head
            while n:
                if n.data < 2:
                    n = n.ref
                elif n.data == 2:
                    print(n.data, "is prime")
                else:
                    is_prime = True
                    for i in range(2, n.data - 1):
                        if n.data % i == 0:
                            is_prime = False
                    if is_prime:
                        print(n.data, "is prime")
                n = n.ref

    def middle_element(self):
        if self.head is None:
            print("LL is empty")
        else:
            fast = self.head
            slow = self.head

            while fast  and fast.ref :

                slow = slow.ref
                fast = fast.ref.ref

            return slow.data

    def has_cycle(self):
        if self.head is None:
            print("Ll is empty")
        else:
            fast = self.head
            slow = self.head

            while fast and fast.ref:
                fast = fast.ref.ref
                slow = slow.ref

            if slow == fast:
                print("LL has cycle")
            print("LL has no cycle")


LL1 = LinkedList()
LL1.add_begin(1)
LL1.add_begin(2)
LL1.add_end(10)
LL1.add_end(11)
LL1.add_begin(45)
LL1.add_after(4, 2)
LL1.add_before(5, 11)
LL1.largest_element()
LL1.second_largest()
print("middle eleement is", LL1.middle_element())
LL1.has_cycle()
LL1.print_list()
