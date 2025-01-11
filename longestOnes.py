# pylint: skip-file

'''
1004. Max Consecutive Ones III

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 
Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
'''

from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, max_window_length, zeros_count = 0, 0, 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros_count += 1
            while zeros_count > k:
                if nums[left] == 0:
                    zeros_count -= 1
                left += 1
            if (right - left + 1) > max_window_length:
                max_window_length = (right - left + 1)
        return max_window_length


if __name__ == "__main__":
    nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    k = 3
    print(f'nums: {nums}')
    print(f'k: {k}')
    solution = Solution()
    OUTPUT = solution.longestOnes(nums, k)
    print(f'longestOnes: {OUTPUT}')
    EXPECTED_OUTPUT = 10
    print(f'Expected Output: {EXPECTED_OUTPUT}')
    print(f'OUTPUT == EXPECTED_OUTPUT: {OUTPUT == EXPECTED_OUTPUT}')