'''find_three_largest_nums.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
print(" ")

'''
given an array of three or more integers
without sorting the array
return a sorted array of the three largest integers

return duplicate integers if necessary
'''

# Time: O(n) | # Space: O(1)


def findThreeLargestNumbers(array):
    three_largest_nums = [-999999999, -999999999, -999999999]

    for num in array:
        min_large_num = min(three_largest_nums)

        for idx, large_num in enumerate(three_largest_nums):
            if large_num == min_large_num:
                if num > min_large_num:
                    three_largest_nums[idx] = num
                break

        three_largest_nums.sort()

    return three_largest_nums


arr = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
print(findThreeLargestNumbers(arr))
print(" ")
