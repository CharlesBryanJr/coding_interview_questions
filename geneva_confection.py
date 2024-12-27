'''geneva_confection..py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=C0303
print(" ")

ingredients = 0

sample_input1 =[2, 
                4,
                2, 3, 1, 4,
                4,
                4,
                4, 1, 3, 2] 

sample_input2 =[2, 
                4,
                2, 3, 1, 4]

def find_lowest_ingredient(lowest_ingredient, mountain_top, branch):
    #lowest_ingredient = mountain_top[0]
    for current_ingredient in mountain_top:
        if current_ingredient < lowest_ingredient:
            lowest_ingredient = current_ingredient
    
    for current_ingredient in branch:
        if current_ingredient < lowest_ingredient:
            lowest_ingredient = current_ingredient
    
    return lowest_ingredient

def geneva_confection(test):

    result = False

    test_cases = test[0]
    n = test[1]
    count_to_n = 0
    test_idx = 0
    ingredients = []
    mountain_top = []
    branch = []
    lake = []

    for num in test:
        test_idx += 1
        if test_idx > 2:
            ingredients.append(num)
            mountain_top.append(num)
    
    mountain_top.reverse()

    while len(mountain_top) != 0 or len(branch) != 0:

        if len(mountain_top) != 0:
            lowest_ingredient = mountain_top[0]
            lowest_ingredient = find_lowest_ingredient(lowest_ingredient, mountain_top, branch)
            print(lowest_ingredient)

            mountain_top_copy = mountain_top[:]
            for ingredient in mountain_top_copy:

                if ingredient == lowest_ingredient:
                    lake.append(ingredient)
                    mountain_top.remove(ingredient)
                    print(mountain_top)
                    print(branch)
                    print(lake)
                    print(" ")
                    
                else:
                    branch.append(ingredient)
                    mountain_top.remove(ingredient)
                    print(mountain_top)
                    print(branch)
                    print(lake)
                    print(" ")
                
            branch.reverse()

    
        elif len(branch) != 0:
            lowest_ingredient = branch[0]
            lowest_ingredient = find_lowest_ingredient(lowest_ingredient, mountain_top, branch)
            print(lowest_ingredient)

            branch_copy = branch[:]
            for ingredient in branch_copy:

                if ingredient == lowest_ingredient:
                    lake.append(ingredient)
                    branch.remove(ingredient)
                    print(mountain_top)
                    print(branch)
                    print(lake)
                    print(" ")
                else:
                    print(mountain_top)
                    print(branch)
                    print(lake)
                    print(" ")
                    #return False
        

    print(mountain_top)
    print(branch)
    print(lake)
    return result
                
print(geneva_confection(sample_input1))
print(" ")
print(" ")
print(" ")
print(geneva_confection(sample_input2))
print(" ")

