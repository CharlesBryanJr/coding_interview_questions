'''longestPeak.py'''
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


Input():
# Intuitive
    -  an array of integers
# Primitive Types
		# Numbers
			# Zero (0)
			# NULL or nil
			# Negative Numbers
			# Floats or Doubles (clarifies if Ints only?)
			# Min/Max Int

Observations / Clarifying Questions / Insights:
- peak ==
    - adjacent integers that strictly increase until the tip
    - then
    - adjacent integers that strictly decreasing
- tip == highest value in the peak
- 3 integer minimum

Cases:
#

# simplest / smallest problem
	#

# If I knew / had this....
	# reverse this statement

Output(int): longest_peak_length
- the length of the longest peak in the array

'''

'''
Algo Time: O() | # Space: O():
Main Function
Input():
find all peaks
compare all peaks
return the length of the largest one

Output(int): longest_peak_length
- the length of the longest peak in the array
'''

# Time: O(n) | # Space: O(1)
def longestPeak(array):
    longest_peak = float('-inf')
    peaks = []
    i = 1
    while i < len(array) - 1:
        if array[i] > array[i - 1] and array[i] > array[i + 1]:
            peaks.append(i)
        i += 1
    if not peaks:
        return 0
    for peak in peaks:
        peak_length = 1
        peak_length += count_right(peak, array)
        peak_length += count_left(peak, array)
        if peak_length > longest_peak:
            longest_peak = peak_length
    return longest_peak

def count_right(peak, array):
    count = 0
    for i in range(peak, len(array) - 1):
        if array[i] > array[i + 1]:
            count += 1
        else:
            break
    return count

def count_left(peak, array):
    count = 0
    for i in reversed(range(1, peak + 1)):
        if array[i] > array[i - 1]:
            count += 1
        else:
            break
    return count

def longestPeak_recursion(array):
    peaks = count_peaks(1, array, [])
    if not peaks:
        return 0
    return find_longest_peaks(0, peaks, float('-inf'), array)

def count_peaks(i, array, peaks):
    if i >= len(array) - 1:
        return peaks
    isPeak = array[i] > array[i - 1] and array[i] > array[i + 1]
    if isPeak:
        peaks.append(i)
    return count_peaks(i + 1, array, peaks)

def find_longest_peaks(peak, peaks, longest_peak, array):
    if peak >= len(peaks):
        return longest_peak
    peak_length = 1
    peak_length += count_length_right(peaks[peak], 0, array)
    peak_length += count_length_left(peaks[peak], 0, array)
    if peak_length > longest_peak:
        longest_peak = peak_length
    return find_longest_peaks(peak + 1, peaks, longest_peak, array)

def count_length_right(idx, length, array):
    if idx >= len(array) - 1:
        return length
    is_decreasing = array[idx] > array[idx + 1]
    if is_decreasing:
        length += 1
    else:
        return length
    return count_length_right(idx + 1, length, array)

def count_length_left(idx, length, array):
    if idx <= 0:
        return length
    is_decreasing = array[idx] > array[idx - 1]
    if is_decreasing:
        length += 1
    else:
        return length
    return count_length_left(idx - 1, length, array)


array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
print("array:", array)
print("longestPeak:", longestPeak(array))
print("longestPeak_recursion:", longestPeak_recursion(array))
print(" ")

array = [1, 2, 3, 3, 2, 1]
print("array:", array)
print("longestPeak:", longestPeak(array))
print("longestPeak_recursion:", longestPeak_recursion(array))
print(" ")

array = [1, 1, 1, 2, 3, 10, 12, -3, -3, 2, 3, 45, 800, 99, 98, 0, -1, -1, 2, 3, 4, 5, 0, -1, -1]
print("array:", array)
print("longestPeak:", longestPeak(array))
print("longestPeak_recursion:", longestPeak_recursion(array))
print(" ")
