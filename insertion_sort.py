'''insertion_sort'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
print(" ")

'''
given an array of integers
return the given array sorted
'''

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

# Time: O(n^2) | # Space: O(1)
def insertionSort(array):

    for i in range(1, len(array)):
        j = i

        # while the current index is not at the beginning of the array
        # check if current number is less than the number before it
            # if so, swap
            # decrement the current index
        while j > 0 and array[j] < array[j - 1]:
            swap(j, j - 1, array)
            j -= 1

    return array


arr = [8, 5, 2, 9, 5, 6, 3]
print("before:",arr)
print("after:",insertionSort(arr))
print(" ")