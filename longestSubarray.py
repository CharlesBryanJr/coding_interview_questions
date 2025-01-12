# pylint: skip-file

'''
1493. Longest Subarray of 1's After Deleting One Element

Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 
Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
 
Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
'''

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, zeros_count, max_length = 0, 0, 0
        for right, value in enumerate(nums):
            if value == 0:
                zeros_count += 1
            while zeros_count > 1:
                if nums[left] == 0:
                    zeros_count -= 1
                left += 1
            max_length = max(max_length, right - left)
        return max_length


if __name__ == "__main__":
    nums = [0,1,1,1,0,1,1,0,1]
    print(f'nums: {nums}')
    solution = Solution()
    OUTPUT = solution.longestSubarray(nums)
    print(f'longestSubarray: {OUTPUT}')
    EXPECTED_OUTPUT = 5
    print(f'Expected Output: {EXPECTED_OUTPUT}')
    print(f'OUTPUT == EXPECTED_OUTPUT: {OUTPUT == EXPECTED_OUTPUT}')