'''minimum_wait_time.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
print(" ")

# Time: O(V+E) | # Space: O(V)

# given a non empty array of postive integers
# postive integers represent the amount of time specfic queries wait before executing

# only one query can be excuted at a time
# queries can be excuted in any order 

# return the minimum amount of total waiting time for all of the queries 

# For each index, sum all of the integers prior and add it to the minimum_wait_time

def minimumWaitingTime(queries):
    minimum_wait_time = 0
    queries.sort()

    for idx, query in enumerate(queries):
        if idx == 0:
            pass

        copy_queries = queries[:idx]
        minimum_wait_time += sum(copy_queries)

    return minimum_wait_time


queries = [3, 2, 1, 2, 6]
print(minimumWaitingTime(queries))

print(" ")