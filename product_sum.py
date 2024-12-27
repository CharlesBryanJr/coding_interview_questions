'''product_sum.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
print(" ")

# given a "special" array return its product sum
# "special" array == non empty of ints or other "special" arrays
# Time: O(V+E) | # Space: O(V)
def productSum(array, multipler=1):
    product_sum = 0

    for element in array:
        if isinstance(element, int):
            product_sum += element
        else:
            product_sum += productSum(element, multipler + 1)


    return product_sum * multipler

arr = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
print(productSum(arr))
print(" ")
