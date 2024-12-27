'''subarraySort.py'''
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

# Searching
# Sorting
# Stacks

Input(array): array
# Intuitive
	# array of integers
		# at least two integers
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
# in place sorting?
# smallest subarray?
# starting and ending indices
# a single number can NOT be out of sorted order
# only pairs of numbers can not be in sorted order
# if one number is not in sorted order
# the subarray that needs to be sorted will depend upon
    # the final postions of the max and min of the unsorted numbers

Cases:
#

# simplest / smallest problem
	#

# If I knew / had this....
	#
	# reverse this statement

Output(array): array
# starting and ending indices of the smallest subarray that needs to be sorted in place
# so that the entire input array would be sorted
'''

'''
# Time: O(n) | # Space: O(1)
Main Function
Input(array): array

Iterate through the entire array, starting at 0
    # to to find all the numbers that are not sorted,
    # reduce the problem to, is the current number sorted

    determine if the current number is sorted
    # IF the current num is
    # greater or equal to the last num
    # AND
    # less than or equal to the next num
    # THEN the current number is sorted

        if the current number is not sorted,
        # the current number is potentially the
        # max or min of the unsorted,
        # which will deteremine the start or end index
        # of the unsorted subarry

            if the current num < min
                update min == current num
                # the min value will be used later to determine
                # the start index of the unsorted subarry

            if the current num > max
                update max == current num
                # the max value will be used later to determine
                # the end index of the unsorted subarray

        DO NOTHING,
        # if the current number is sorted,
        # related to it's adjacent numbers

    Iterate through the entire array,
    starting at 0
        # with the known min value of the unsorted subarray
        # loop the array from 0th index
        # and determine the min value's correct index

        if num >= min
            # then we have found the correct index of the min value

            append the min value to the output array

    Iterate through the entire array in REVERSED order,
    starting at the end
        # with the known max value of the unsorted subarray
        # loop the array from the last index
        # and determine the min value's correct index

        if num <= max
            # then we have found the correct index of the max value

            append the max value to the output array


Output(array): array
# starting and ending indices of the smallest subarray
that needs to be sorted in place
so that the entire input array would be sorted
'''

# find all the unsorted numbers
# find the smallest and largest unsorted numbers
# find the sorted index for the smallest and largest unsorted numbers

# Time: O(n) | # Space: O(1)
def subarraySort(array):
    min_unsorted = float('inf')
    max_unsorted = float('-inf')
    for i in range(len(array)):
        num = array[i]
        if is_unsorted(i, num, array):
            min_unsorted = min(num, min_unsorted)
            max_unsorted = max(num, max_unsorted)

    if min_unsorted == float('inf') and max_unsorted == float('-inf'):
        return [-1, -1]

    min_sorted_idx = 0
    while array[min_sorted_idx] <= min_unsorted:
        min_sorted_idx += 1

    max_sorted_idx = len(array) - 1
    while array[max_sorted_idx] >= max_unsorted:
        max_sorted_idx -= 1

    return [min_sorted_idx, max_sorted_idx]


def is_unsorted(i, num, array):
    if i == 0:
        return num > array[i + 1]
    if i == len(array) - 1:
        return num < array[i - 1]
    return num > array[i + 1] or num < array[i - 1]

# _recursion
# _iteration

array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
print("array:", array)
print("subarraySort:", subarraySort(array))
'''
print("sub_array_sort:", sub_array_sort_iteration(array))
print(" ")

array = [4, 8, 7, 12, 11, 9, -1, 3, 9, 16, -15, 51, 7]
print("array:", array)
print("subarraySort:", subarraySort(array))
print("sub_array_sort:", sub_array_sort_iteration(array))
print(" ")

array = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print("array:", array)
print("subarraySort:", subarraySort(array))
print("sub_array_sort:", sub_array_sort_iteration(array))
print(" ")
'''