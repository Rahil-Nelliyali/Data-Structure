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

    def delete(self, data):
        if data < self.key:
            # Value is smaller, so we need to go left.
            if self.left:
                self.left = self.left.delete(data)
            else:
                # Value not found in the BST.
                return self
        elif data > self.key:
            # Value is greater, so we need to go right.
            if self.right:
                self.right = self.right.delete(data)
            else:
                # Value not found in the BST.
                return self
        else:
            # We found the node to delete.
            if not self.left and not self.right:
                # Node is a leaf, simply delete it.
                return None
            elif not self.left:
                # Node has no left child, replace it with the right child.
                return self.right
            elif not self.right:
                # Node has no right child, replace it with the left child.
                return self.left
            else:
                # Node has both left and right children.
                # Find the minimum value in the right subtree (the smallest value greater than the current node).
                min_node = self.right.smallest_node()

                # Replace the current node's key with the minimum value found.
                self.key = min_node.key
                # Delete the minimum node from the right subtree.
                self.right = self.right.delete(min_node.key)
        return self

    def smallest_node(self):
        current = self
        while current.left:
            current = current.left
        return current

    def largest_node(self):
        current = self
        while current.right:
            current = current.right
        return current

    def find_closest_value(self, target):
        closest = self.key
        current = self

        while current:
            if abs(target - current.key) < abs(target - closest) and current.key != target:
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


def is_valid_bst(root1):
    def is_valid(node, min_val, max_val):
        if node is None:
            return True
        if node.key <= min_val or node.key >= max_val:
            return False
        return is_valid(node.left, min_val, node.key) and is_valid(node.right, node.key, max_val)

    return is_valid(root1, float('-inf'), float('inf'))


root = BST(10)
list1 = [20, 11, 6, 13, -1, 8, 12000, 15]
for i in list1:
    root.insert(i)
root.search(60)

print("After deletion: ")
if count(root) > 1:
    root.delete(10)
else:
    print("Can't perform deletion operation")
print("---pre order-----")

root.pre_order_traversal()

root.smallest_node()
root.largest_node()

result = is_valid_bst(root)

if result is True:
    print("BST is valid")
else:
    print("BST not valid")

print(root.find_closest_value(30))
