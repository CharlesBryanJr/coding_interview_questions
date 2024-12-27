'''firstDuplicateValue.py'''
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
Question:
-

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

# Recursion
	# the solution depends on solutions to smaller instances of the same problem
		# define the smaller instance of the problem
			# translate the for/while loop into a base case
	# will iterate/traverse until the function can return a value (base case)
		# always include return statment
	# base case == the smallest instance of the problem that can be solved directly
	# to keep track of element, store the element in a variable that connected to the recursion call
	# running variables left to right
			# arguments
	# running variables right to left
			# return statment
	# Recursive functions often take a sub array of the original array
	# the outcome of a recursive function will affect code on lines after it
	# To optimize use memoization
		# store the answer to recursive calls in a hash table
	# 1. Base Case
	# 2. Action
	# 3. update variables
	# 4. Recursion
		if idx >= len(array):

# Searching
# Sorting


Input():
# Intuitive
- array of integers between 1 and n, inclusive
- n == length of the array

# Primitive Types
		# Numbers
			# Zero (0)
			# NULL or nil
			# Negative Numbers
			# Floats or Doubles (clarifies if Ints only?)
			# Min/Max Int
		# Arrays
			# Empty array
			# Nested or not nested


Observations / Clarifying Questions / Insights:
# from left to right
# mutate the input array if needed
# since the nums in the array are limited from 1 to n
	each idx can represent a num

Cases:
#

# simplest / smallest problem
	#

# If I knew / had this....
	#
	# reverse this statement

Output(int): num
- return -1, if no duplicates exist
- return num, if duplicates exist
'''

'''
# Time: O() | # Space: O()
Main Function
Input(array): array

Output(int): num
- return -1, if no duplicates exist
- return num, if duplicates exist
'''


# Time: O(n) | # Space: O(n)
def firstDuplicateValue_n(array):
    nums = {}
    for num in array:
        if num in nums:
            return num
        nums[num] = True
    return -1

# Time: O(n) | # Space: O(n)
def first_Duplicate_Value_recursion(array):
    if len(array) < 2:
        return -1
    return find_first_duplicate(1, array[0], -1, array, {})

def find_first_duplicate(i, num, duplicate, array, nums):
    is_duplicate = num in nums
    if is_duplicate:
        duplicate = num
    end_of_array = i >= len(array)
    if is_duplicate or end_of_array:
        return duplicate
    nums[num] = True
    return find_first_duplicate(i + 1, array[i], duplicate, array, nums)

# Time: O(n) | # Space: O(1)
def firstDuplicateValue(array):
    for num in array:
        abs_value = abs(num)
        is_duplicate = array[abs_value - 1] < 0
        if is_duplicate:
            return abs_value
        array[abs_value - 1] *= -1
    return -1

# Time: O(n) | # Space: O(1)
def firstDuplicateValue_recursion(array):
    no_duplicate = -1
    duplicate = find_duplicate(0, array)
    if duplicate:
        return duplicate
    else:
        return no_duplicate


def find_duplicate(i, array):
    end_of_array = i >= len(array)
    if end_of_array:
        return -1
    abs_value = abs(array[i])
    is_duplicate = array[abs_value - 1] < 0
    if is_duplicate or end_of_array:
        return abs_value
    array[abs_value - 1] *= -1
    return find_duplicate(i + 1, array)


array = [2, 1, 5, 2, 3, 3, 4]
print("array:", array)
print("firstDuplicateValue_n:", firstDuplicateValue_n(array))
print("first_Duplicate_Value_recursion:", first_Duplicate_Value_recursion(array))
print("firstDuplicateValue:", firstDuplicateValue(array))
print("firstDuplicateValue_recursion:", firstDuplicateValue_recursion(array))
print(" ")

array = [2, 2, 2, 2, 2, 2, 2, 2, 2]
print("array:", array)
print("firstDuplicateValue_n:", firstDuplicateValue_n(array))
print("first_Duplicate_Value_recursion:", first_Duplicate_Value_recursion(array))
print("firstDuplicateValue:", firstDuplicateValue(array))
print("firstDuplicateValue_recursion:", firstDuplicateValue_recursion(array))
print(" ")

array = [4, 7, 7, 14, 14, 10, 15, 14, 14, 16, 14, 11, 5, 12, 17, 7, 1, 6, 13]
print("array:", array)
print("firstDuplicateValue_n:", firstDuplicateValue_n(array))
print("first_Duplicate_Value_recursion:", first_Duplicate_Value_recursion(array))
print("firstDuplicateValue:", firstDuplicateValue(array))
print("firstDuplicateValue_recursion:", firstDuplicateValue_recursion(array))
print(" ")
