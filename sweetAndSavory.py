'''sweetAndSavory'''
# pylint: disable=C0114
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
# pylint: disable=C0304
# pylint: disable=E0401
print(" ")

'''
Question:
- given an array of numbers (numbers represent dishes)
- return an numbers array of len(2), 
which represent the desired sweet and savory combination 
that the customer is looking for.  

Type of Question:
- array

Clarifying Questions / Insights:
- each number is non zero
- a neg num == sweet dish
- a post num == savory dish
- abs value of num == how sweet or how savory the dish is
- In the output array, one dish must be sweet
- In the output array, one dish must be savory
- The output needs to be the closet lower sum

Base case:
-

Edge cases:
-


Input:
- Intuitive
- Primitive Types
		- Numbers
			- Zero (0)
			- Negative Numbers
			- Min/Max Int
		- Arrays
			- Empty array
			- Nested or not nested

- If I knew / had this....
	-

Output:
-
'''


# Time: O(n^2) | # Space: O(1)
def sweetAndSavory_nn_1(dishes, target):
    best_dishes = [0, 0]
    if len(dishes) < 2:
        return best_dishes

    dishes.sort()
    best_flavor = float('inf')

    for i in range(len(dishes)):
        if dishes[i] < 0:
            continue
        flavor_change = i
        break

    for left in range(0, flavor_change):
        for right in range(flavor_change, len(dishes)):
            flavor = dishes[left] + dishes[right]
            if flavor > target:
                continue

            diff = target - flavor
            if diff == 0:
                return [dishes[left], dishes[right]]

            if diff < best_flavor:
                best_flavor = diff
                best_dishes[0] = dishes[left]
                best_dishes[1] = dishes[right]

    return best_dishes


# Time: O(nlogn) | # Space: O(n)
def sweetAndSavory_nlogn_n(dishes, target):
    best_dishes = [0, 0]
    if len(dishes) < 2:
        return best_dishes

    sweet = []
    savory = []

    for num in dishes:
        if num < 0:
            sweet.append(num)
        else:
            savory.append(num)

    sweet.sort(reverse=True)
    savory.sort()

    best_flavor = float('inf')

    i, ii = 0, 0
    while i < len(sweet) and ii < len(savory):
        flavor = sweet[i] + savory[ii]
        if flavor > target:
            i += 1
        elif flavor < target:
            diff = abs(flavor - target)
            if diff < best_flavor:
                best_flavor = diff
                best_dishes[0] = sweet[i]
                best_dishes[1] = savory[ii]
            ii += 1
        else:
            return [sweet[i], savory[ii]]

    return best_dishes


dishes = [5, 2, -7, 30, 12, -4, -20]
target = 4
print("dishes:", dishes)
print("target:", target)
print("sweetAndSavory_nn_1:", sweetAndSavory_nn_1(dishes, target))
dishes = [5, 2, -7, 30, 12, -4, -20]
target = 4
print("sweetAndSavory_nlogn_n:", sweetAndSavory_nlogn_n(dishes, target))
print(" ")

dishes = [5, -5, 5, -5, 5, -5]
target = 0
print("dishes:", dishes)
print("target:", target)
print("sweetAndSavory_nn_1:", sweetAndSavory_nn_1(dishes, target))
dishes = [5, -5, 5, -5, 5, -5]
target = 0
print("sweetAndSavory_nlogn_n:", sweetAndSavory_nlogn_n(dishes, target))
print(" ")

dishes = [-3, -5, 1, 7]
target = 8
print("dishes:", dishes)
print("target:", target)
print("sweetAndSavory_nn_1:", sweetAndSavory_nn_1(dishes, target))
dishes = [-3, -5, 1, 7]
target = 8
print("sweetAndSavory_nlogn_n:", sweetAndSavory_nlogn_n(dishes, target))
print(" ")