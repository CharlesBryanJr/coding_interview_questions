'''bubble_sort.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
print(" ")

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

# Time: O(n^2) | # Space: O(1)


def bubbleSort(array, n=0):
    swap_count = 0
    array_length = len(array)

    for idx, num in enumerate(array):
        if idx + 1 == array_length - abs(n):
            break

        next_idx = idx + 1
        next_num = array[next_idx]

        if num > next_num:
            swap_count += 1
            swap(idx, next_idx, array)

    if swap_count > 0:
        bubbleSort(array, n-1)

    return array


arr = [8, 5, 2, 9, 5, 6, 3]
print("before:", arr)
print("after:", bubbleSort(arr))
print(" ")
