'''two_number_sum.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
# pylint: disable=C0304
# pylint: disable=C0200
# pylint: disable=E101
print(" ")

'''

Question:
-

Type of Question:
- Array
- draw indices
	- sorting
    - multiple pointers

Input:
- Intuitive
    - non empty array of distinct ints
    - int, represent the target sum
- Primitive Types
	- Numbers
		- Zero (0)
		- NULL or nil
		- Negative Numbers
		- Floats or Doubles (clarifies if Ints only?)
		- Min/Max Int
	- Arrays
		- Empty array
		- Nested or not nested

Observations / Clarifying Questions / Insights:
- the same index can not be used twice

Output:
- array of two ints that sum up to the target sum
- empty array if no two ints sum up to the target sum
'''


# O(n^2) time | O(1) space
def two_number_sum_n_n(array, target_sum):
    for i in range(len(array) - 1):
        for ii in range(i + 1, len(array)):
            if array[i] + array[ii] == target_sum:
                return [array[i], array[ii]]
    return []


# O(n) time | O(n) space
def twoNumberSum_n(array, targetSum):
    nums = {}
    for num in array:
        potential_match = targetSum - num
        if potential_match in nums:
            return [potential_match, num]
        else:
            nums[num] = True
    return []


# O(nlog(n)) time | O(1) space
def twoNumberSum3_nlogn(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        num1 = array[left]
        num2 = array[right]
        if num1 + num2 < targetSum:
            left += 1
        elif num1 + num2 > targetSum:
            right -= 1
        elif num1 + num2 == targetSum:
            return [num1, num2]
    return []


array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10
print("array:", array)
print("targetSum:", targetSum)
print("two_number_sum_n_n:", two_number_sum_n_n(array, targetSum))
print("twoNumberSum_n:", twoNumberSum_n(array, targetSum))
print("twoNumberSum3_nlogn:", twoNumberSum3_nlogn(array, targetSum))
print(" ")

array = [4, 6, 1, -3]
targetSum = 3
print("array:", array)
print("targetSum:", targetSum)
print("two_number_sum_n_n:", two_number_sum_n_n(array, targetSum))
print("twoNumberSum_n:", twoNumberSum_n(array, targetSum))
print("twoNumberSum3_nlogn:", twoNumberSum3_nlogn(array, targetSum))
print(" ")

array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 15
print("array:", array)
print("targetSum:", targetSum)
print("two_number_sum_n_n:", two_number_sum_n_n(array, targetSum))
print("twoNumberSum_n:", twoNumberSum_n(array, targetSum))
print("twoNumberSum3_nlogn:", twoNumberSum3_nlogn(array, targetSum))
print(" ")

# _recursion
# _iteration
