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

# Time: O(nlog(n)) | # Space: O(nlog(n))
def mergeSort(array):
    base_case = (len(array) == 1)
    if base_case:
        return array

    middle_idx = len(array) // 2
    left = array[:middle_idx]
    right = array[middle_idx:]
    return merge_sorted_arrays_1(mergeSort(left), mergeSort(right))


def merge_sorted_arrays_1(left, right):
    sorted_array = [None] * (len(left) + len(right))
    i = j = k = 0
    left_in_range = j < len(left)
    right_in_range = k < len(right)
    while left_in_range and right_in_range:
        if left[j] <= right[k]:
            sorted_array[i] = left[j]
            j += 1
        else:
            sorted_array[i] = right[k]
            k += 1
        i += 1
        left_in_range = j < len(left)
        right_in_range = k < len(right)

    left_in_range = j < len(left)
    while left_in_range:
        sorted_array[i] = left[j]
        j += 1
        i += 1
        left_in_range = j < len(left)

    right_in_range = k < len(right)
    while right_in_range:
        sorted_array[i] = right[k]
        k += 1
        i += 1
        right_in_range = k < len(right)

    return sorted_array


def merge_sort(array):
    base_case = (len(array) == 1)
    if base_case:
        return array

    middle_idx = len(array) // 2
    left = array[:middle_idx]
    right = array[middle_idx:]
    return merge_sorted_arrays_2(merge_sort(left), merge_sort(right))


def merge_sorted_arrays_2(left, right):
    sorted_array = []

    j = k = 0
    left_in_range = j < len(left)
    right_in_range = k < len(right)

    while left_in_range and right_in_range:
        if left[j] <= right[k]:
            sorted_array.append(left[j])
            j += 1
        else:
            sorted_array.append(right[k])
            k += 1
        left_in_range = j < len(left)
        right_in_range = k < len(right)

    if left_in_range:
        sorted_array += left[j:]

    if right_in_range:
        sorted_array += right[k:]

    return sorted_array


array = [8, 5, 2, 9, 5, 6, 3]
print("array:", array)
print("mergeSort:", mergeSort(array))
print("merge_sort:", merge_sort(array))
print(" ")

array = [5, -2, 2, -8, 3, -10, -6, -1, 2, -2, 9, 1, 1]
print("array:", array)
print("mergeSort:", mergeSort(array))
print("merge_sort:", merge_sort(array))
print(" ")

array = [-823, 164, 48, -987, 323, 399, -293, 183, -908, -376, 14, 980, 965, 842, 422, 829, 59, 724, -415, -733, 356, -855, -155, 52, 328, -544, -371, -160, -942, -51, 700, -363, -353, -359, 238, 892, -730, -575, 892, 490, 490, 995, 572, 888, -935, 919, -191, 646, -120, 125, -817, 341, -575, 372, -874, 243, 610, -36, -685, -337, -13, 295, 800, -950, -949, -257, 631, -542, 201, -796, 157, 950, 540, -846, -265, 746, 355, -578, -441, -254, -941, -738, -469, -167, -420, -126, -410, 59]
print("array:", array)
print("mergeSort:", mergeSort(array))
print("merge_sort:", merge_sort(array))
print(" ")