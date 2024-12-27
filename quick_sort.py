'''merge_sort'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0621
# pylint: disable=W0102
print(" ")

'''
- What: A precise specification of the problem that the algorithm solves.
given an array of integers return a sorted version of the the input array

- How: A precise description of the algorithm itself.

Merge Sort
1. Divide the input array into two subarrays of roughly equal size.
2. Recursively merge sort each of the subarrays.
3. Merge the newly-sorted subarrays into a single sorted array.

- Why: A proof that the algorithm solves the problem it is supposed to solve.

- How fast: An analysis of the running time of the algorithm.

note:
-
'''

# Time: O(n^2) | # Space: O(log(n))
def quickSort(array):
    quick_sort(0, len(array) - 1, array)
    return array

def quick_sort(start, end, array):
    if start >= end:
        return

    pivot = start
    left = pivot + 1
    right = end

    while left <= right:
        if array[left] > array[pivot] and array[right] < array[pivot]:
            swap(left, right, array)

        if array[left] <= array[pivot]:
            left += 1
        elif array[right] >= array[pivot]:
            right -= 1

    swap(pivot, right, array)

    is_left_subarray_smaller = right - 1 - start < end - (right + 1)
    if is_left_subarray_smaller:
        quick_sort(start, right - 1, array)
        quick_sort(right + 1, end, array)
    else:
        quick_sort(right + 1, end, array)
        quick_sort(start, right - 1, array)

    return


def swap(i, ii, array):
    array[i], array[ii] = array[ii], array[i]
    return

array = [8, 5, 2, 9, 5, 6, 3]
print("array:", array)
print("quickSort:", quickSort(array))
array = [8, 5, 2, 9, 5, 6, 3]
print("quickSort:", quickSort(array))
print(" ")

array = [5, -2, 2, -8, 3, -10, -6, -1, 2, -2, 9, 1, 1]
print("array:", array)
print("quickSort:", quickSort(array))
array = [5, -2, 2, -8, 3, -10, -6, -1, 2, -2, 9, 1, 1]
print("quickSort:", quickSort(array))
print(" ")

array = [-823, 164, 48, -987, 323, 399, -293, 183, -908, -376, 14, 980, 965, 842, 422, 829, 59, 724, -415, -733, 356, -855, -155, 52, 328, -544, -371, -160, -942, -51, 700, -363, -353, -359, 238, 892, -730, -575, 892, 490, 490, 995, 572, 888, -935, 919, -191, 646, -120, 125, -817, 341, -575, 372, -874, 243, 610, -36, -685, -337, -13, 295, 800, -950, -949, -257, 631, -542, 201, -796, 157, 950, 540, -846, -265, 746, 355, -578, -441, -254, -941, -738, -469, -167, -420, -126, -410, 59]
print("array:", array)
print("quickSort:", quickSort(array))
array = [-823, 164, 48, -987, 323, 399, -293, 183, -908, -376, 14, 980, 965, 842, 422, 829, 59, 724, -415, -733, 356, -855, -155, 52, 328, -544, -371, -160, -942, -51, 700, -363, -353, -359, 238, 892, -730, -575, 892, 490, 490, 995, 572, 888, -935, 919, -191, 646, -120, 125, -817, 341, -575, 372, -874, 243, 610, -36, -685, -337, -13, 295, 800, -950, -949, -257, 631, -542, 201, -796, 157, 950, 540, -846, -265, 746, 355, -578, -441, -254, -941, -738, -469, -167, -420, -126, -410, 59]
print("quickSort:", quickSort(array))
print(" ")
