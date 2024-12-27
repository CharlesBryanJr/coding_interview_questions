'''pleasnt_multiply'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0621
# pylint: disable=W0102
print(" ")


'''
- What: A precise specification of the problem that the algorithm solves.
given two postive integers, multiply them and return the result

- How: A precise description of the algorithm itself.

Peasant Multiply

- Why: A proof that the algorithm solves the problem it is supposed to solve.

- How fast: An analysis of the running time of the algorithm.

note:
-
'''

def PeasantMultiply_iteration(x, y):
    product = 0
    while x > 0:
        x_isOdd = (x % 2 != 0)
        if x_isOdd:
            product += y
        x //= 2
        y += y
    return product


def PeasantMultiply_recursion(x, y):
    if x <= 0:
        return 0
    else:
        x //= 2
        y += y
        product = PeasantMultiply_recursion(x, y)
        x_isOdd = (x % 2 != 0)
        if x_isOdd:
            product += y
    return product


x = 84
y = 12
print("x:", x)
print("y:", y)
print("PeasantMultiply_iteration:", PeasantMultiply_iteration(x, y))
print("PeasantMultiply_recursion:", PeasantMultiply_recursion(x, y))
print(" ")

x = 33
y = 47
print("x:", x)
print("y:", y)
print("PeasantMultiply_iteration:", PeasantMultiply_iteration(x, y))
print("PeasantMultiply_recursion:", PeasantMultiply_recursion(x, y))
print(" ")

x = 3423419
y = 1034023
print("x:", x)
print("y:", y)
print("PeasantMultiply_iteration:", PeasantMultiply_iteration(x, y))
print("PeasantMultiply_recursion:", PeasantMultiply_recursion(x, y))
print(" ")

