'''hasSingleCycle.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
# pylint: disable=C0304
print(" ")

'''

given:
- an array of integers

note:
- each given integer represents a jump
- a jump can wrap
- single cycle == 
    - starting at any index
    - if the following jumps visit each index once

action:
- visit n elements
- while n < visited > 0
    - and we are back at starting point, return False
- if visited >= n and we are not back at starting point, return False

return:
- True, if the jumps form a single cycle
- False, if the jumps do NOT form a single cycle


- visit n elements
- 
'''

# Time: O(n^2) | # Space: O(n)
def hasSingleCycle_n2_n(array):
    visited_index = {}
    
    for idx, num in enumerate(array):
        visited_index[idx] = False
    
    for idx, num in enumerate(array):
        jump = num
        next_idx = idx + jump
        while next_idx < 0:
            next_idx = len(array) - abs(next_idx)
        while next_idx > len(array) - 1:
            next_idx = next_idx - len(array)
        if visited_index[next_idx] == True:
            return False
        else:
            visited_index[next_idx] = True

    return True

# Time: O(n^2) | # Space: O(1)
def hasSingleCycle_n2_1(array):

    for idx, num in enumerate(array):
        jump = int(num)
        next_idx = idx + jump
        while next_idx < 0:
            next_idx = len(array) - abs(next_idx)
        while next_idx > len(array) - 1:
            next_idx = next_idx - len(array)
            
        if isinstance(array[next_idx], str):
            return False
        else:
            array[next_idx] = str(array[next_idx])

    return True

# Time: O(n) | # Space: O(1)
def hasSingleCycle(array):
    visited_elements = 0
    starting_idx = 0
    current_idx = starting_idx
    
    while visited_elements < len(array):
        if visited_elements > 0 and current_idx == starting_idx:
            return False
        
        visited_elements += 1
        current_idx = get_next_idx(current_idx, array)
    
    return current_idx == starting_idx

def get_next_idx(current_idx, array):
    jump = array[current_idx]
    next_idx = (current_idx + jump) % len(array)
    return next_idx if next_idx >= 0 else next_idx + len(array)

array = [1, -1, 1, -1]
print("array:", array)
print("hasSingleCycle_n2_n:", hasSingleCycle_n2_n(array))
print("hasSingleCycle_n2_1:", hasSingleCycle_n2_1(array))
print("hasSingleCycle:", hasSingleCycle(array))
print(" ")

'''
array = [0, 1, 1, 1, 1]
print("array:", array)
print("hasSingleCycle_n2_n:", hasSingleCycle_n2_n(array))
print("hasSingleCycle_n2_1:", hasSingleCycle_n2_1(array))
print("hasSingleCycle:", hasSingleCycle(array))
print(" ")

array = [1, 2, 3, 4, -2, 3, 7, 8, -26]
print("array:", array)
print("hasSingleCycle_n2_n:", hasSingleCycle_n2_n(array))
print("hasSingleCycle_n2_1:", hasSingleCycle_n2_1(array))
print("hasSingleCycle:", hasSingleCycle(array))
print(" ")
'''