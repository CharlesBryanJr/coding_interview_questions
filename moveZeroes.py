# pylint: skip-file

'''
283. Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you minimize the total number of operations done?
'''


from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        char_to_move, char_to_move_count, non_char_to_move_idx = 0, 0, 0
        for i in range(len(nums)):
            if nums[i] == char_to_move:
                char_to_move_count += 1
            else:
                nums[non_char_to_move_idx] = nums[i]
                non_char_to_move_idx += 1    
        char_to_move_idx = len(nums) - 1
        while char_to_move_count > 0:
            nums[char_to_move_idx] = char_to_move
            char_to_move_idx -= 1
            char_to_move_count -= 1
        return nums


if __name__ == "__main__":
    nums = [0,1,0,3,12]
    print(f'nums: {nums}')
    solution = Solution()
    OUTPUT = solution.moveZeroes(nums)
    print(f'moveZeroes: {OUTPUT}')
    EXPECTED_OUTPUT = [1,3,12,0,0]
    print(f'Expected Output: {EXPECTED_OUTPUT}')
    print(f'OUTPUT == EXPECTED_OUTPUT: {OUTPUT == EXPECTED_OUTPUT}')