'''file_name'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
print(" ")

# given a sorted array and a target number
# find the target number

# m = (l+r) // 2

# Time: O(log(n)) | # Space: O(1)


def binary_search_iterative(array, target):
    array.sort()
    left = 0
    right = len(array)-1

    while left <= right:

        middle = (left + right) // 2
        potenital_match = array[middle]

        if potenital_match == target:
            return middle

        if potenital_match > target:
            right = middle - 1

        else:  # potenital_match < target:
            left = middle + 1

    return -1

# Time: O(log(n)) | # Space: O(log(n))


def binary_search_recursion(array, target, left, right):

    if left > right:
        return -1

    middle = (left + right) // 2
    potenital_match = array[middle]

    if potenital_match == target:
        return middle

    elif potenital_match > target:
        return binary_search_recursion(array, target, left, (middle-1))

    else:  # potenital_match < target:
        return binary_search_recursion(array, target, (middle+1), right)


def binarySearch(array, target):
    array.sort()
    return binary_search_recursion(array, target, 0, len(array)-1)


arr = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
t = 33
print(binarySearch(arr, t))
print(binary_search_iterative(arr, t))

print(" ")
