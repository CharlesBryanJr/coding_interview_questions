'''file_name'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
print(" ")

'''
given:
- a non empty array of integers

action:
- using the given array, construct a binary search tree

return:
- a pre order binary search tree

note:
- order of integers represent the order they were visisted during a pre order traversal.
- if the numbers are getting smaller, I am going down the left side
- first number is the root node
- left child = the first number less than the current node
- right child = the first number greater than or equal the current node

Pre - Order
1. Visit
2. Left
3. Right

'''
# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Time: O(n^2) | # Space: O(h)
def reconstructBst_n_n(preOrderTraversalValues):
    if len(preOrderTraversalValues) == 0:
        return None

    current_value = preOrderTraversalValues[0]
    right_sub_tree_root_idx = len(preOrderTraversalValues)

    for idx in range(1, len(preOrderTraversalValues)):
        value = preOrderTraversalValues[idx]
        if value >= current_value:
            right_sub_tree_root_idx = idx
            break

    left_sub_tree = reconstructBst_n_n(preOrderTraversalValues[1:right_sub_tree_root_idx])
    right_sub_tree = reconstructBst_n_n(preOrderTraversalValues[right_sub_tree_root_idx:])

    return BST(current_value, left_sub_tree, right_sub_tree)

class TreeInfo:
    def __init__(self, root_idx) -> None:
        self.root_idx = root_idx

def reconstruct_bst(lower_bound, upper_bound, preOrderTraversalValues, sub_tree_info):
    if sub_tree_info.root_idx == len(preOrderTraversalValues):
        return None
    
    root_value = preOrderTraversalValues[sub_tree_info.root_idx]
    if root_value < lower_bound or root_value >= upper_bound:
        return None
    
    sub_tree_info.root_idx += 1
    left_sub_tree = reconstruct_bst(lower_bound, root_value, preOrderTraversalValues, sub_tree_info)
    right_sub_tree = reconstruct_bst(root_value, upper_bound, preOrderTraversalValues, sub_tree_info)

    return BST(root_value, left_sub_tree, right_sub_tree)

# Time: O(n) | # Space: O(h)
def reconstructBst(preOrderTraversalValues):
    if len(preOrderTraversalValues) == 0:
        return None
    tree_info = TreeInfo(0)
    lower_bound = float("-inf")
    upper_bound = float("inf")
    return reconstruct_bst(lower_bound, upper_bound, preOrderTraversalValues, tree_info)


array = [10, 4, 2, 1, 5, 17, 19, 18]
print("array:", array)
print("reconstructBst_n_n:", reconstructBst_n_n(array))
print("reconstructBst:", reconstructBst(array))
print(" ")

array = [5, -10, -5, 6, 9, 7]
print("array:", array)
print("reconstructBst_n_n:", reconstructBst_n_n(array))
print("reconstructBst:", reconstructBst(array))
print(" ")

array = [2, 0, 1, 3, 4, 3]
print("array:", array)
print("reconstructBst_n_n:", reconstructBst_n_n(array))
print("reconstructBst:", reconstructBst(array))
print(" ")

# _recursion
# _iteration
print(" ")