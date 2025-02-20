# pylint: skip-file
'''
11. Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
'''

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j, max_area = 0, len(height) - 1, -1
        while i < j:
            area = abs(i - j) * min(height[i], height[j])
            if area > max_area:
                max_area = area
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area


if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    print(f'height: {height}')
    solution = Solution()
    OUTPUT = solution.maxArea(height)
    print(f'maxArea: {OUTPUT}')
    EXPECTED_OUTPUT = 49
    print(f'Expected Output: {OUTPUT == EXPECTED_OUTPUT}')