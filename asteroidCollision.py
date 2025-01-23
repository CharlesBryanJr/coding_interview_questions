# pylint: skip-file

'''
735. Asteroid Collision

We are given an array asteroids of integers representing asteroids in a row. The indices of the asteriod in the array represent their relative position in space.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
 

Constraints:

2 <= asteroids.length <= 104
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0
'''

from typing import List
from typing import Tuple


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n, i = len(asteroids), 1
        if n <= 1:
            return asteroids
        res = [asteroids[0]]
        while i < n :
            print(f'i: {i}')
            print(f'res[-1]: {res[-1]}')
            print(f'asteroids[i]: {asteroids[i]}')
            if res[-1] > 0 and asteroids[i] < 0:
                if abs(res[-1]) < abs(asteroids[i]):
                    res.pop()
                    res.append(asteroids[i])
                elif abs(res[-1]) == abs(asteroids[i]):
                    res.pop()
            else:
                res.append(asteroids[i])
            print(f'res: {res}')
            print()
            i += 1
        return res


if __name__ == "__main__":
    asteroids = [10,2,-5]
    print(f'asteroids: {asteroids}')
    solution = Solution()
    OUTPUT = solution.asteroidCollision(asteroids)
    print(f'asteroidCollision: {OUTPUT}')
    EXPECTED_OUTPUT = [10]
    print(f'Expected Output: {EXPECTED_OUTPUT}')
    print(f'OUTPUT == EXPECTED_OUTPUT: {OUTPUT == EXPECTED_OUTPUT}')