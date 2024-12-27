'''zero_sum_subarray.py'''
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

Input(array): nums
# Intuitive
    # an array of numbers

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
		# Dictionaries (Hashmaps)
			# Collisions

Observations / Clarifying Questions / Insights:
# zero sum subarray == all values add to zero
# subarray == any contiguous section of the array

Cases:
#

# simplest / smallest problem
	#

# If I knew / had this....
	#
	# reverse this statement

Output(boolean):
    # True, if a zero sum subarray exist
    # False, if a zero sum subarray does not exist
'''

'''
# Time: O() | # Space: O()
Main Function
Input(array): nums

Output(boolean):
    # True, if a zero sum subarray exist
    # False, if a zero sum subarray does not exist
'''


# Time: O(n) | # Space: O(n)
def zeroSumSubarray_iteration(nums):
    running_sums = set([0])
    running_sum = 0
    for num in nums:
        running_sum += num
        if running_sum in running_sums:
            return True
        running_sums.add(running_sum)
    return False


def zeroSumSubarray_recursion(nums):
    return isZeroSumSubarray(0, 0, set([0]), nums)


def isZeroSumSubarray(i, running_sum, running_sums, nums):
    out_of_range = i >= len(nums)
    if out_of_range:
        return False
    running_sum += nums[i]
    if running_sum in running_sums:
        return True
    running_sums.add(running_sum)
    return isZeroSumSubarray(i + 1, running_sum, running_sums, nums)


nums = [1, 2, -2, 3]
print("nums:", nums)
print("zeroSumSubarray_iteration:", zeroSumSubarray_iteration(nums))
print("zeroSumSubarray_recursion:", zeroSumSubarray_recursion(nums))
print(" ")

nums = [-1, 2, 3, 4, -5, -3, 1, 2]
print("nums:", nums)
print("zeroSumSubarray_iteration:", zeroSumSubarray_iteration(nums))
print("zeroSumSubarray_recursion:", zeroSumSubarray_recursion(nums))
print(" ")

nums = [1, 2, 3, 4, 0, 5, 6, 7]
print("nums:", nums)
print("zeroSumSubarray_iteration:", zeroSumSubarray_iteration(nums))
print("zeroSumSubarray_recursion:", zeroSumSubarray_recursion(nums))
print(" ")