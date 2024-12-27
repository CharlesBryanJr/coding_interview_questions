'''numberOfWaysToMakeChange.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
print(" ")

'''

given:
- an array of distinct postive integers
    - coin denominaitons

- non negative integer
    - target amount of money

action:
-

return:
- the number of ways to make change for the target amount

note:
- unlimited amount of coins


'''

# Time: O(nd) | # Space: O(n)


def numberOfWaysToMakeChange(n, denoms):
    ways = [1] + [0 for _ in range(n)]

    for denom in denoms:
        for amount in range(denom, n + 1):
            print("denom:", denom)
            print("amount:", amount)
            print("amount - denom:", amount - denom)
            print(" ")
            ways[amount] += ways[amount - denom]

    print("ways:", ways)
    return ways[n]


n = 10
denoms = [1, 5, 10, 25]
print("n:", n)
print("denoms:", denoms)
print("numberOfWaysToMakeChange:", numberOfWaysToMakeChange(n, denoms))
print(" ")

n = 12
denoms = [2, 3, 7]
print("n:", n)
print("denoms:", denoms)
print("numberOfWaysToMakeChange:", numberOfWaysToMakeChange(n, denoms))
print(" ")

n = 7
denoms = [2, 3, 4, 7]
print("n:", n)
print("denoms:", denoms)
print("numberOfWaysToMakeChange:", numberOfWaysToMakeChange(n, denoms))
print(" ")

# _recursion
# _iteration
print(" ")
