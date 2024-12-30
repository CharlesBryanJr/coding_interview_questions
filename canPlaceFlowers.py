'''
605. Can Place Flowers

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 

Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        visited = flowerbed[]
        print(f'visited: {visited}')

        available_flower_spots_count = 0
        for i in range(1, len(flowerbed) - 1):
            left, right = i - 1, i + 1
            visited[left], visited[i], visited[right] = True, True, True
            can_place_flower = True if (flowerbed[left] == 0 and flowerbed[i] == 0 and flowerbed[right] == 0) else False

            if can_place_flower:
                print('can_place_flower at index:', i)
                available_flower_spots_count += 1
                print('available_flower_spots_count:', available_flower_spots_count)

        return True
'''

from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:    
        if n == 0:
            return True
        for i in range(len(flowerbed)):
            is_left_empty = (i == 0 or flowerbed[i - 1] == 0)
            is_right_empty = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
            if flowerbed[i] == 0 and is_left_empty and is_right_empty:
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
        return False


if __name__ == "__main__":
    flowerbed = [0,0,1,0,1]
    n = 2
    solution = Solution()
    print(f'canPlaceFlowers: {solution.canPlaceFlowers(flowerbed, n)}')