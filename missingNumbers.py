'''missingNumbers.py'''
# pylint: disable=C0114
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
# pylint: disable=C0304
# pylint: disable=E0401
print(" ")

'''

Type of Question:
-

Clarifying Questions / Insights:
-

Edge cases:
-

Base case:
-

Question:
-


'''

'''
Algo Time: O() | # Space: O():
-
-
    - Input:
        -
        -
    - Output:
'''


# _recursion
# Time: O(n) | # Space: O(n)
def missingNumbers_n_n(nums):
    min = 1
    max = len(nums) + 2
    missing_numbers = [num for num in range(min, max + 1)]
    for num in nums:
        if num in missing_numbers:
            missing_numbers.remove(num)
    return missing_numbers


def missingNumbers_n_n_recursion(nums):
    min = 1
    max = len(nums) + 2
    missing_numbers = [num for num in range(min, max + 1)]
    return find_missing_nums(0, nums, missing_numbers)

def find_missing_nums(i, nums, missing_numbers):
    if i >= len(nums):
        return missing_numbers
    if nums[i] in missing_numbers:
        missing_numbers.remove(nums[i])
    return find_missing_nums(i + 1, nums, missing_numbers)


# Time: O(n) | # Space: O(1)
def missingNumbers_n_1(nums):
    nums += [1, 1]
    missing_numbers = []
    for i in range(len(nums)):
        num_map_to_idx = abs(nums[i]) - 1
        nums[num_map_to_idx] *= -1
    for i in range(len(nums)):
        is_missing_number = nums[i] > 0
        if is_missing_number:
            missing_number = i + 1
            missing_numbers.append(missing_number)
    return missing_numbers

def missingNumbers_n_1_recursion(nums):
    nums += [1, 1]
    identify_present_nums(0, nums)
    return find_missing_nums_n_1_recursion(0, nums, [])


def identify_present_nums(i, nums):
    out_of_range = (i >= len(nums))
    if out_of_range:
        return
    num = abs(nums[i])
    num_map_to_idx = num - 1  # map number to an index
    nums[num_map_to_idx] *= -1
    return identify_present_nums(i + 1, nums)

def find_missing_nums_n_1_recursion(i, nums, missing_numbers):
    out_of_range = (i >= len(nums))
    if out_of_range:
        return missing_numbers

    num_map_to_idx = nums[i]
    is_missing_number = num_map_to_idx > 0
    if is_missing_number:
        missing_number = i + 1  # unmap idx to find missing number
        missing_numbers.append(missing_number)

    return find_missing_nums_n_1_recursion(i + 1, nums, missing_numbers)

def missingNumbers(nums):
    min = 1
    max = len(nums) + 3
    total = sum(range(1, len(nums) + 3))
    for num in nums:
        total -= num

    avg_missing_value = total // 2

    found_first_half_num = 0
    found_second_half_num = 0

    for num in nums:
        if num <= avg_missing_value:
            found_first_half_num += num
        else:
            found_second_half_num += num

    expected_first_half_sum = sum(range(1, avg_missing_value + 1))
    expected_second_half_sum = sum(range(avg_missing_value + 1, len(nums) + 3))

    return [expected_first_half_sum - found_first_half_num, expected_second_half_sum - found_second_half_num]


nums = [3, 5, 1, 2, 4, 7, 6]
print("nums:", nums)
print("missingNumbers_n_n:", missingNumbers_n_n(nums))
print("missingNumbers_n_n_recursion:", missingNumbers_n_n_recursion(nums))
print("missingNumbers_n_1:", missingNumbers_n_1(nums))
print("missingNumbers_n_1_recursion:", missingNumbers_n_1_recursion([3, 5, 1, 2, 4, 7, 6]))
print("missingNumbers:", missingNumbers([3, 5, 1, 2, 4, 7, 6]))
print(" ")

nums = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("nums:", nums)
print("missingNumbers_n_n:", missingNumbers_n_n(nums))
print("missingNumbers_n_n_recursion:", missingNumbers_n_n_recursion(nums))
print("missingNumbers_n_1:", missingNumbers_n_1(nums))
print("missingNumbers_n_1_recursion:", missingNumbers_n_1_recursion([11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print("missingNumbers:", missingNumbers([11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(" ")

nums = [4, 5, 3]
print("nums:", nums)
print("missingNumbers_n_n:", missingNumbers_n_n(nums))
print("missingNumbers_n_n_recursion:", missingNumbers_n_n_recursion(nums))
print("missingNumbers_n_1:", missingNumbers_n_1(nums))
print("missingNumbers_n_1_recursion:", missingNumbers_n_1_recursion([4, 5, 3]))
print("missingNumbers:", missingNumbers([4, 5, 3]))
print(" ")