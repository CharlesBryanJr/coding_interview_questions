'''binary_search_tree.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
print(" ")

# NODE
# 1. Value
# 2. Left pointer
# 3. Right pointer

# add LEFT if node is less than root node
# add RIGHT if node is greater than root node

class Node:

    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


class BST:

    def __init__(self):
        self.root = None

    def add(self, current_node, new_node_value):

        if self.root is None:
            self.root = Node(new_node_value)
            return None

        if new_node_value < current_node.value:

            if current_node.left is None:
                current_node.left = Node(new_node_value)

            else:  # if current_node.left exist
                self.add(current_node.left, new_node_value)

        else:  # new_node_value > current_node.value

            if current_node.right is None:
                current_node.right = Node(new_node_value)

            else:  # if current_node.right exist
                self.add(current_node.right, new_node_value)

        return None


    def visit(self, node):
        print(node.value)
    
    def preorder(self, current):
        # Pre Order Traversal
        # 1. Visit
        # 2. Go Left
        # 3. Go Right
        # 4. Go Back
        self.visit(current)
        self.preorder(current.left)
        self.preorder(current.right)

    def postorder(self, current):
        # Post Order Traversal
        # 1. Go Left
        # 2. Go Right
        # 3. Visit
        # 4. Go Back
        self.postorder(current.left)
        self.postorder(current.right)
        self.visit(current)

    def inorder(self, current):
        # In Order Traversal
        # 1. Go Left
        # 2. Visit
        # 3. Go Right
        # 4. Go Back
        self.inorder(current.left)
        self.visit(current)
        self.inorder(current.right)


t1 = BST()

print(" ")
