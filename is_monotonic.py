'''is_monotonic.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
# pylint: disable=C0304
# pylint: disable=C0200
print(" ")

'''
given:
-  an array of integers


Type of Question:
- Array
		- draw indices
		- sorting
    - multiple pointers
    - mutating the current index or later index to count
    - hashing the index values
		- running sums
		- sliding windows
			- start_of_window
			- end_of_window

Input:
- Intuitive
- Primitive Types
		- Numbers
			- Zero (0)
			- NULL or nil
			- Negative Numbers
			- Floats or Doubles (clarifies if Ints only?)
			- Min/Max Int

Observations / Clarifying Questions / Insights:
    - elements are non increasing from left to right
        - elements to the right do not increase
        - elements to the right are less than or equal to the the current number
            - num >= next_num
    - elements are non decreasing from left to right
        - elements to the right do not decrease
        - elements to the right are greater than or equal to the the current number
            - num <= next_num

return:
- boolean True if monotonic
- boolean False if not monotonic
'''


# Time: O(n) | # Space: O(1)
def isMonotonic(array):
    if len(array) <= 1:
        return True
    return non_decreasing(array) or non_increasing(array)

def non_decreasing(array):
    last_num = array[0]
    for num in array:
        if num < last_num:
            return False
        last_num = num
    return True

def non_increasing(array):
    last_num = array[0]
    for num in array:
        if num > last_num:
            return False
        last_num = num
    return True

array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
print("array:", array)
print("isMonotonic:", isMonotonic(array))
print(" ")

array = [2, 2, 2, 1, 4, 5]
print("array:", array)
print("isMonotonic:", isMonotonic(array))
print(" ")

array = [1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 11]
print("array:", array)
print("isMonotonic:", isMonotonic(array))
print(" ")
