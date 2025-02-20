# pylint: skip-file

'''
238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 
Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
'''

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        running_product = 1
        for i in range(len(nums)):
            answer[i] = running_product
            running_product *= nums[i]
        running_product = 1
        for i in reversed(range(len(nums))):
            answer[i] *= running_product
            running_product *= nums[i]
        return answer


if __name__ == "__main__":
    nums = [-1,1,0,-3,3]
    print(f'nums: {nums}')
    solution = Solution()
    OUTPUT = solution.productExceptSelf(nums)
    print(f'productExceptSelf: {OUTPUT}')
    EXPECTED_OUTPUT = [0,0,9,0,0]
    print(f'Expected Output: {OUTPUT == EXPECTED_OUTPUT}')
