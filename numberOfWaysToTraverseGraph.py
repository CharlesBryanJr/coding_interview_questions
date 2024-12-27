'''numberOfWaysToTraverseGraph.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
print(" ")

'''

given:
- given the dimensions of a rectangular grid
    - width and height
    - postive integers
-

action:
-

return:
- starting from the top left corner, count the number of ways to reach the bottom right corner of the grid

note:
- only moves, go right or go down
- width * height >= 2
-


'''

# Time: O(2^(n + m)) | # Space: O(n + m)
def numberOfWaysToTraverseGraph_recursion(width, height):
    # Write your code here.
    if width == 1 or height == 1:
        return 1

    left = numberOfWaysToTraverseGraph_recursion(width-1, height)
    up = numberOfWaysToTraverseGraph_recursion(width, height-1)

    return left + up

# Time: O(n * m) | # Space: O(n * m)
def numberOfWaysToTraverseGraph_iteration(width, height):
    ways = [[0 for box in range(width + 1)] for box in range(height + 1)]

    for width_idx in range(1, width + 1):
        for height_idx in range(1, height + 1):

            if width_idx == 1 or height_idx == 1:
                ways[height_idx][width_idx] = 1

            else:
                left = ways[height_idx][width_idx - 1]
                up = ways[height_idx - 1][width_idx]
                ways[height_idx][width_idx] = left + up

    return ways[height_idx][width_idx]

# Permutations
    # For the known frequency of two unqiue elements
    # their different combinations are as follows:
    # (R + D)! / R! * D!

# Time: O(n + m) | # Space: O(1)
def numberOfWaysToTraverseGraph_loop(width, height):
    permutations = 0
    right_moves_to_corner = width - 1
    down_moves_to_corner = height - 1
    width_factorial = 1
    height_factorial = 1
    width_plus_height_factorial = 1

    for num in range(2, right_moves_to_corner + down_moves_to_corner + 1):
        if num < right_moves_to_corner + 1:
            width_factorial *= num
        if num < down_moves_to_corner + 1:
            height_factorial *= num

        width_plus_height_factorial *= num

    permutations = width_plus_height_factorial // (width_factorial * height_factorial)

    return permutations


def factorial(num):
    result = 1

    for n in range(2, num + 1):
        result *= n

    return result

# Time: O(n + m) | # Space: O(1)
def numberOfWaysToTraverseGraph(width, height):
    right_moves_to_corner = width - 1
    down_moves_to_corner = height - 1

    numerator = factorial(right_moves_to_corner + down_moves_to_corner)
    denominator = factorial(right_moves_to_corner) * factorial(down_moves_to_corner)

    return numerator // denominator


width = 4
height = 3
print("width:", width)
print("height:", height)
print("numberOfWaysToTraverseGraph_recursion:", numberOfWaysToTraverseGraph_recursion(width, height))
print("numberOfWaysToTraverseGraph_iteration:", numberOfWaysToTraverseGraph_iteration(width, height))
print("numberOfWaysToTraverseGraph_loop:", numberOfWaysToTraverseGraph_loop(width, height))
print("numberOfWaysToTraverseGraph:", numberOfWaysToTraverseGraph(width, height))
print(" ")

width = 3
height = 3
print("width:", width)
print("height:", height)
print("numberOfWaysToTraverseGraph_recursion:", numberOfWaysToTraverseGraph_recursion(width, height))
print("numberOfWaysToTraverseGraph_iteration:", numberOfWaysToTraverseGraph_iteration(width, height))
print("numberOfWaysToTraverseGraph_loop:", numberOfWaysToTraverseGraph_loop(width, height))
print("numberOfWaysToTraverseGraph:", numberOfWaysToTraverseGraph(width, height))
print(" ")

width = 5
height = 9
print("width:", width)
print("height:", height)
print("numberOfWaysToTraverseGraph_recursion:", numberOfWaysToTraverseGraph_recursion(width, height))
print("numberOfWaysToTraverseGraph_iteration:", numberOfWaysToTraverseGraph_iteration(width, height))
print("numberOfWaysToTraverseGraph_loop:", numberOfWaysToTraverseGraph_loop(width, height))
print("numberOfWaysToTraverseGraph:", numberOfWaysToTraverseGraph(width, height))
print(" ")

# _recursion
# _iteration
print(" ")
