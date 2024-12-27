'''minNumberOfCoinsForChange.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
print(" ")

'''

given:
-
action:
-
return:
-
note:
-


'''

# Time: O() | # Space: O()


def minNumberOfCoinsForChange(n, denoms):
    num_of_coins = [float("inf") for amount in range(n + 1)]
    num_of_coins[0] = 0

    for denom in denoms:
        for amount in range(len(num_of_coins)):
            if denom <= amount:
                num_of_coins[amount] = min(
                    num_of_coins[amount], 1 + num_of_coins[amount - denom])

    return num_of_coins[n] if num_of_coins[n] != float("inf") else - 1


n = 7
denoms = [1, 5, 10]
print("n:", n)
print("denoms:", denoms)
print("minNumberOfCoinsForChange:", minNumberOfCoinsForChange(n, denoms))
print(" ")

n = 9
denoms = [3, 4, 5]
print("n:", n)
print("denoms:", denoms)
print("minNumberOfCoinsForChange:", minNumberOfCoinsForChange(n, denoms))
print(" ")

n = 135
denoms = [39, 45, 130, 40, 4, 1]
print("n:", n)
print("denoms:", denoms)
print("minNumberOfCoinsForChange:", minNumberOfCoinsForChange(n, denoms))
print(" ")

# _recursion
# _iteration
print(" ")
