'''findClosestValueInBst.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
print(" ")

# assume that there is only one closet value

# O(1) time | O(1) space


def findClosestValueInBst(tree, target):
    # Write your code here.
    closest_value = None
    smallest_abs_difference = 1000000
    abs_difference = 0
    current_node = tree

    while current_node is not None:

        if current_node.value == target:
            closest_value = current_node.value
            break
        
        abs_difference = abs(current_node.value - target)
        
        if abs_difference < smallest_abs_difference:
            smallest_abs_difference = abs_difference
            closest_value = current_node.value
        

        if target < current_node.value:
            current_node = current_node.left

        else:
            current_node = current_node.right

    return closest_value


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


print(" ")
