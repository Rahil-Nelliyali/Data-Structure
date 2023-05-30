class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def in_order_traversal(node, result):
    if node:
        in_order_traversal(node.left, result)
        result.append(node.value)
        in_order_traversal(node.right, result)

def height(node):
    if node is None:
        return 0
    return max(height(node.left), height(node.right)) + 1

def is_balanced(node):
    if node is None:
        return True
    left_height = height(node.left)
    right_height = height(node.right)
    if abs(left_height - right_height) <= 1 and is_balanced(node.left) and is_balanced(node.right):
        return True
    return False

def find_lca(node, n1, n2):
    if node is None:
        return None
    if node.value == n1 or node.value == n2:
        return node
    left_lca = find_lca(node.left, n1, n2)
    right_lca = find_lca(node.right, n1, n2)
    if left_lca and right_lca:
        return node
    return left_lca if left_lca else right_lca

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

result = []
in_order_traversal(root, result)
print(result)  

print(is_balanced(root))  

lca = find_lca(root, 4, 5)
print('Lowest common ancestor: ',lca.value)  


