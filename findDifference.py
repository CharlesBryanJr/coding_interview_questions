# pylint: skip-file

'''

'''

from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        return [[]]


if __name__ == "__main__":
    nums1 = [1,2,3]
    nums2 = [2,4,6]
    print(f'nums1: {nums1}')
    print(f'nums2: {nums2}')
    solution = Solution()
    OUTPUT = solution.findDifference(nums1, nums2)
    print(f'findDifference: {OUTPUT}')
    EXPECTED_OUTPUT = [[1,3],[4,6]]
    print(f'Expected Output: {EXPECTED_OUTPUT}')
    print(f'OUTPUT == EXPECTED_OUTPUT: {OUTPUT == EXPECTED_OUTPUT}')