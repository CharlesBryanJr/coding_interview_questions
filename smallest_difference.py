'''smallest_difference.pyx'''
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
- two non empty arrays of integers
- find a pair of numbers (one from each given array)

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

Observations / Clarifying Questions / Insights:
- absoulte difference == distance between two numbers on a number line
    - absoulte_difference = abs(a - b)
- for two sorted arrays
    - determine which number is the largest and increment the other num
        - this will bring the other number closer to the first num
        - and therefore decrease the smallest difference

Output:
- pair of numbers (one from each given array)
- absoulte value is closest to zero
- order of return array matters
'''

# Time: O(nlog(n) + mlog(m)) | # Space: O(1)
def smallestDifference(arrayOne, arrayTwo):
    smallest_difference = float('inf')
    smallest_difference_array = []
    arrayOne.sort()
    arrayTwo.sort()
    i, ii = 0, 0
    while i < len(arrayOne) and ii < len(arrayTwo):
        if abs(arrayOne[i] - arrayTwo[ii]) < smallest_difference:
            smallest_difference = abs(arrayOne[i] - arrayTwo[ii])
            smallest_difference_array = [arrayOne[i], arrayTwo[ii]]
        if arrayOne[i] < arrayTwo[ii]:
            i += 1
        else:
            ii += 1
    return smallest_difference_array


arrayOne = [-1, 5, 10, 20, 28, 3]
print("arrayOne:", arrayOne)
arrayTwo = [26, 134, 135, 15, 17]
print("arrayTwo:", arrayTwo)
print("smallestDifference:", smallestDifference(arrayOne, arrayTwo))
print(" ")

arrayOne = [10, 0, 20, 25]
print("arrayOne:", arrayOne)
arrayTwo = [1005, 1006, 1014, 1032, 1031]
print("arrayTwo:", arrayTwo)
print("smallestDifference:", smallestDifference(arrayOne, arrayTwo))
print(" ")

arrayOne = [10, 1000, 9124, 2142, 59, 24, 596, 591, 124, -123]
print("arrayOne:", arrayOne)
arrayTwo = [-1441, -124, -25, 1014, 1500, 660, 410, 245, 530]
print("arrayTwo:", arrayTwo)
print("smallestDifference:", smallestDifference(arrayOne, arrayTwo))
print(" ")