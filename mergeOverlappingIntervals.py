'''merge_overlapping_intervals.py'''
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
    # a non empty two dimensional array of aribitary intervals

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
# interval == two integers
# interval[0] = start of interval
# interval[1] = end of interval

Cases:
#

# simplest / smallest problem
	#

# If I knew / had this....
	#
	# reverse this statement


Output(array): overlapping_intervals
# new intervals in any order
'''

'''
# Time: O(nlog(n)) | # Space: O(n)
Main Function
Input(array): intervals

    # sort the array so that the start of each interval is in ascending order
        # we can sort this 2D array by using the lambda function


    # we need an array data structure to store our output overlapping_intervals array

    # next, we need to create a varaible that will store the current interval
        # the current interval will be the last interval that was appended to our output array
        # the current interval's start will remain constant
        # the current interval's end can and will be updated if needed

    # append the current interval to the array
        # after the input has been sorted
            # the first interval's start will be the smallest value
            # and the smallest value should be also the first interval's start in the output array

    # iterate through the sorted intervals
        # if the current_interval_end >= interval_start:
            # then, we have found an overlapping interval
            # We need to update the current_interval_end in the output array
                # if current_interval_end > interval_end
                    # then the interval is encompassed within the current interval in the output array
                    # so no update if needed
                # if the interval_end > current_interval_end
                    # then we need to expand the current_interval_end
                    # so, update current_interval_end == interval_end
        # if the current_interval_end < interval_start:
            # then its time to append the interval
            # update current_interval == interval
                # because we are done with the old current_interval
                # and the next iteration needs the an updated current_interval
            # append the current_interval to the output array
                # the current_interval's start is now the smallest value remaining
                # if need the current_interval's end will be updated

Output(array): overlapping_intervals
# new intervals in any order
'''


# Time: O(nlog(n)) | # Space: O(n)
def merge_overlapping_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    result = [intervals[0]]
    for interval in intervals:
        overlapping_interval = interval[0] <= result[-1][1]
        if overlapping_interval:
            result[-1][1] = max(result[-1][1], interval[1])
        else:
            result.append(interval)
    return result


# Time: O(nlog(n)) | # Space: O(n)
def mergeOverlappingIntervals_recursive(intervals):
    intervals.sort(key=lambda x: x[0])
    return update_intervals(1, intervals, [intervals[0]])

def update_intervals(i, intervals, overlapping_intervals):
    end_of_array = i >= len(intervals)
    if end_of_array:
        return overlapping_intervals

    overlapping_interval = intervals[i][0] <= overlapping_intervals[-1][1]
    if overlapping_interval:
        overlapping_intervals[-1][1] = max(overlapping_intervals[-1][1], intervals[i][1])
    else:
        overlapping_intervals.append(intervals[i])

    return update_intervals(i + 1, intervals, overlapping_intervals)


intervals = [[1, 2],
             [3, 5],
             [4, 7],
             [6, 8],
             [9, 10]]
print("intervals:", intervals)
print("merge_overlapping_intervals", merge_overlapping_intervals(intervals))
print("mergeOverlappingIntervals_recursive:", mergeOverlappingIntervals_recursive(intervals))
print(" ")

intervals = [[0, 0],
             [0, 0],
             [0, 0],
             [0, 0],
             [0, 0],
             [0, 0],
             [0, 1]]
print("intervals:", intervals)
print("merge_overlapping_intervals", merge_overlapping_intervals(intervals))
print("mergeOverlappingIntervals_recursive:", mergeOverlappingIntervals_recursive(intervals))
print(" ")

intervals = [
    [89, 90],
    [-10, 20],
    [-50, 0],
    [70, 90],
    [90, 91],
    [90, 95]
]
print("intervals:", intervals)
print("merge_overlapping_intervals", merge_overlapping_intervals(intervals))
print("mergeOverlappingIntervals_recursive:", mergeOverlappingIntervals_recursive(intervals))
print(" ")

intervals = [
    [1, 22],
    [-20, 30]
]
print("intervals:", intervals)
print("merge_overlapping_intervals", merge_overlapping_intervals(intervals))
print("mergeOverlappingIntervals_recursive:", mergeOverlappingIntervals_recursive(intervals))
print(" ")