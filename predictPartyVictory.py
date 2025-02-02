# pylint: skip-file

'''
649. Dota2 Senate

In the world of Dota2, there are two parties: the Radiant and the Dire.

The Dota2 senate consists of senators coming from two parties. Now the Senate wants to decide on a change in the Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can exercise one of the two rights:

Ban one senator's right: A senator can make another senator lose all his rights in this and all the following rounds.
Announce the victory: If this senator found the senators who still have rights to vote are all from the same party, he can announce the victory and decide on the change in the game.
Given a string senate representing each senator's party belonging. The character 'R' and 'D' represent the Radiant party and the Dire party. Then if there are n senators, the size of the given string will be n.

The round-based procedure starts from the first senator to the last senator in the given order. This procedure will last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.

Suppose every senator is smart enough and will play the best strategy for his own party. Predict which party will finally announce the victory and change the Dota2 game. The output should be "Radiant" or "Dire".

 
Example 1:

Input: senate = "RD"
Output: "Radiant"
Explanation: 
The first senator comes from Radiant and he can just ban the next senator's right in round 1. 
And the second senator can't exercise any rights anymore since his right has been banned. 
And in round 2, the first senator can just announce the victory since he is the only guy in the senate who can vote.
Example 2:

Input: senate = "RDD"
Output: "Dire"
Explanation: 
The first senator comes from Radiant and he can just ban the next senator's right in round 1. 
And the second senator can't exercise any rights anymore since his right has been banned. 
And the third senator comes from Dire and he can ban the first senator's right in round 1. 
And in round 2, the third senator can just announce the victory since he is the only guy in the senate who can vote.

Constraints:

n == senate.length
1 <= n <= 104
senate[i] is either 'R' or 'D'.
'''

from typing import List
from typing import Tuple
from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant_queue, dire_queue = deque(), deque()
        radiant_set, dire_set = set(), set()
        n, winner = len(senate), None
        for i in range(n):
            if senate[i] == 'R':
                radiant_queue.append(i)
                radiant_set.add(i)
            else:
                dire_queue.append(i)
                dire_set.add(i)
        i = 0
        while winner is None and i < n:
            print(f'senate {i}: {senate[i]}')
            print(f'radiant_queue: {radiant_queue}')
            print(f'radiant_set: {radiant_set}')
            print(f'dire_queue: {dire_queue}')
            print(f'dire_set: {dire_set}')
            if senate[i] == 'R' and i in radiant_set and dire_queue:
                removed_seantor = dire_queue.popleft()
                dire_set.remove(removed_seantor)
            elif senate[i] == 'D' and i in dire_set and radiant_queue:
                removed_seantor = radiant_queue.popleft()
                radiant_set.remove(removed_seantor)
            i += 1
            print()
        print(f'radiant_queue: {radiant_queue}')
        print(f'radiant_set: {radiant_set}')
        print(f'dire_queue: {dire_queue}')
        print(f'dire_set: {dire_set}')
        return winner


if __name__ == "__main__":
    senate = "DDRRR"
    print(f'senate: {senate}')
    solution = Solution()
    OUTPUT = solution.predictPartyVictory(senate)
    print(f'predictPartyVictory: {OUTPUT}')
    EXPECTED_OUTPUT = "Dire"
    print(f'Expected Output: {EXPECTED_OUTPUT}')
    print(f'OUTPUT == EXPECTED_OUTPUT: {OUTPUT == EXPECTED_OUTPUT}')