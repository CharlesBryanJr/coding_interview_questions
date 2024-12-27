'''selection_sort.py'''
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
def selectionSort(array):
    # for any given index, iterate from the index to the end of the array.
    # find the smallest num
    # swap the given index value with he smallest num
    
    for i in range(0,len(array)-1):
        j = i
        num = array[j]
        smallest_num = array[j]
        found_swap = False

        while j < len(array)-1:
            j += 1
            num = array[j]
            if num < smallest_num:
                smallest_num_index = j
                smallest_num = num
                found_swap = True

        if found_swap is True:
            swap(i, smallest_num_index, array)

    return array


arr = [1, 2]
print("before:",arr)
print("after:",selectionSort(arr))
print(" ")