'''node_depths.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
print(" ")


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Node Depth: the distance between a node in a Binary Tree and the root node
# given a Binary Tree, return the sum of its nodes' depth

# Knowns:
# - root node has a depth of 0
# - the child nodes of the root node have a depth of 0 + 1
# - node_depth = n
# - child_nodes_depth = n + 1

# if current node is none, return none
# RETURN the current nodes' depth
# plus, call the recursive function on both of the current nodes' child nodes
# f(n,d) = d + f(left_node, d+1) + f(right_node, d+1)

# Time: O(n) | # Space: O(h)
def node_depths_recursive(root, total_depth_sum=0):

    if root is None:
        print("Current node is None", root)
        return 0
    
    current_node = root
        
    a = node_depths_recursive(current_node.left, total_depth_sum + 1)
    b = node_depths_recursive(current_node.right, total_depth_sum + 1)

    return total_depth_sum + a + b


# if root node is none, return none
# store the total depth sum in varaible
# create a stack to store the nodes and their depths
# iterate through the node stack
# for each node
    # if the node is none do nothing
    # else increment the total_depth_sum by the running_depth_sum
    # then append the current nodes' left and right node to the stack 
        # and pass the running_depth_sum incremented by 1

def node_depths_iterative(root):

    if root is None:
        print("Root node is None", root)
        return 0

    total_depth_sum = 0

    node_stack = [(root, 0)]

    while len(node_stack) > 0:
        current_node, running_depth_sum = node_stack.pop()

        if current_node is None:
            continue

        total_depth_sum += running_depth_sum
          
        node_stack.append((current_node.left, running_depth_sum + 1))
        node_stack.append((current_node.right, running_depth_sum + 1))
    
    return total_depth_sum

print(" ")