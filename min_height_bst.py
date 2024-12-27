'''min_height_bst.py.py_name'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
import math
print(" ")


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)


# Time: O(nlog(n)) | # Space: O(n)
def minHeightBst_nlog_n(array):
    array_length = len(array)
    bst = None
    start_idx = 0
    end_idx = array_length - 1
    return min_height_bst_nlog_n(array, bst, start_idx, end_idx)


def min_height_bst_nlog_n(array, bst, start_idx, end_idx):
    if end_idx < start_idx:
        return

    middle_idx = math.floor((start_idx + end_idx) / 2)
    value_to_add = array[middle_idx]

    if bst is None:
        bst = BST(value_to_add)
    else:
        bst.insert(value_to_add)

    min_height_bst_nlog_n(array, bst, start_idx, middle_idx - 1)
    min_height_bst_nlog_n(array, bst, middle_idx + 1, end_idx)

    return bst


# Time: O(n) | # Space: O(n)
def minHeightBst_n(array):
    array_length = len(array)
    bst = None
    start_idx = 0
    end_idx = array_length - 1
    return min_height_bst_n(array, bst, start_idx, end_idx)


def min_height_bst_n(array, bst, start_idx, end_idx):
    if end_idx < start_idx:
        return

    middle_idx = math.floor((start_idx + end_idx) / 2)
    new_bst_node = BST(array[middle_idx])

    if bst is None:
        bst = new_bst_node
    else:
        if array[middle_idx] < bst.value:
            bst.left = new_bst_node
            bst = bst.left
        else:
            bst.right = new_bst_node
            bst = bst.right

    min_height_bst_n(array, bst, start_idx, middle_idx - 1)
    min_height_bst_n(array, bst, middle_idx + 1, end_idx)

    return bst


# Time: O(n) | # Space: O(n)
def minHeightBst(array):
    array_length = len(array)
    start_idx = 0
    end_idx = array_length - 1
    return min_height_bst(array, start_idx, end_idx)


def min_height_bst(array, start_idx, end_idx):
    if end_idx < start_idx:
        return None

    middle_idx = math.floor((start_idx + end_idx) / 2)
    bst = BST(array[middle_idx])

    bst.left = min_height_bst(array, start_idx, middle_idx - 1)
    bst.right = min_height_bst(array, middle_idx + 1, end_idx)

    return bst


array = [1, 2, 5, 7, 10, 13, 14, 15, 22]
print("array:", array)
print("minHeightBst_nlog_n:", minHeightBst_nlog_n(array))
print("minHeightBst_n:", minHeightBst_n(array))
print("minHeightBst:", minHeightBst(array))
print(" ")

array = [1, 2, 5, 7, 10, 13, 14, 15, 22, 28]
print("array:", array)
print("minHeightBst_nlog_n:", minHeightBst_nlog_n(array))
print("minHeightBst_n:", minHeightBst_n(array))
print("minHeightBst:", minHeightBst(array))
print(" ")

array = [1, 2, 5, 7, 10, 13, 14, 15, 22, 28, 32, 36, 89, 92, 9000]
print("array:", array)
print("minHeightBst_nlog_n:", minHeightBst_nlog_n(array))
print("minHeightBst_n:", minHeightBst_n(array))
print("minHeightBst:", minHeightBst(array))
print(" ")

# _recursion
# _iteration
print(" ")
