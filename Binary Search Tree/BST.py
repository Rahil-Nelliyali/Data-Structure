class BST:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, data):
        if self.key is None:
            self.key = data
            return

        if self.key == data:
            return  # if data becomes equal

        if data < self.key:
            if self.left:
                self.left.insert(data)
            else:
                self.left = BST(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = BST(data)

    def search(self, data):
        if self.key is None:
            print("Tree is empty")
            return
        if self.key == data:
            print("Node found in tree")
            return
        if data < self.key:
            if self.left:
                self.left.search(data)
            else:
                print("Node not found in the  tree")
        else:
            if self.right:
                self.right.search(data)
            else:
                print("Node not found in  tree")

    def pre_order_traversal(self):
        print(self.key, end=' ')
        if self.left:
            self.left.pre_order_traversal()
        if self.right:
            self.right.pre_order_traversal()

    def in_order_traversal(self):
        if self.left:
            self.left.in_order_traversal()
        print(self.key, end=' ')
        if self.right:
            self.right.in_order_traversal()

    def post_order_traversal(self):
        if self.left:
            self.left.post_order_traversal()
        if self.right:
            self.right.post_order_traversal()
        print(self.key, end=' ')

    def delete(self, data, current):
        if self.key is None:
            print("Tree is empty!")
            return

        if data < self.key:
            if self.left:
                self.left = self.left.delete(data, current)
            else:
                print("Given node is not present in the tree..")
        elif data > self.key:
            if self.right:
                self.right = self.right.delete(data, current)
            else:
                print('Given node is not present in the tree..')
        else:
            if self.left is None:
                temp = self.right
                if data == current:
                    self.key = temp.key
                    self.left = temp.left
                    self.right = temp.right
                    temp = None
                    return
                self = None
                return temp

            if self.right is None:
                temp = self.left
                if data == current:
                    self.key = temp.key
                    self.left = temp.left
                    self.right = temp.right
                    temp = None
                    return
                self = None
                return temp

            node = self.right
            while node.left:
                node = node.left
            self.key = node.key
            self.right = self.right.delete(node.key, current)
        return self

    def smallest_node(self):
        current = self
        while current.left:
            current = current.left
        print("Node with the smallest element: ", current.key)

    def largest_node(self):
        current = self
        while current.right:
            current = current.right
        print("Largest node: ", current.key)

    def validate_bst(self):
        return self._validate_bst_helper(float('-inf'), float('inf'))

    def _validate_bst_helper(self, min_val, max_val):
        if self is None:
            return True

        if self.key <= min_val or self.key >= max_val:
            return False

        left_valid = True
        right_valid = True

        if self.left:
            left_valid = self.left._validate_bst_helper(min_val, self.key)

        if self.right:
            right_valid = self.right._validate_bst_helper(self.key, max_val)

        return left_valid and right_valid

    def find_closest_value(self, target):
        closest = self.key
        current = self

        while current:
            if abs(target - current.key) < abs(target - closest) and current.key!= target:
                closest = current.key

            if target < current.key:
                current = current.left
            elif target > current.key:
                current = current.right
            else:
                break

        return closest


def count(node):
    if node is None:
        return 0
    return 1 + count(node.left) + count(node.right)


root = BST(10)
list1 = [20, 11, 6, 13, -1, 8, 12000, 15]
for i in list1:
    root.insert(i)
root.search(60)

print("After deletion: ")
if count(root) > 1:
    root.delete(10, root.key)
else:
    print("Can't perform deletion operation")
print("---pre order-----")

root.pre_order_traversal()

root.smallest_node()
root.largest_node()

result = root.validate_bst()

if result is True:
    print("BST is valid")
else:
    print("BST not valid")

print(root.find_closest_value(30))
