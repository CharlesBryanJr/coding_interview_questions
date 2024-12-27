'''taskAssignment.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
# pylint: disable=C0304
# pylint: disable=C0200
print(" ")

'''

Question:
- each worker must complete two unique task
- workers can only work on one task at a time
- total number of task == 2 * K
- all tasks are independent
- tasks can be completed in any order
- workers will complete assigned tasks in parallel
- time taken to complete all task == time taken to complete the longest pair of tasks

Type of Question:
- Array
    sorting array

Input:
- Intuitive
    - k == number of workers
    - array of postive integers == durations of tasks
- Primitive Types
		- Numbers
			- Zero (0)
			- NULL or nil
			- Negative Numbers
			- Floats or Doubles (clarifies if Ints only?)
			- Min/Max Int
		- Arrays
			- 1 dimensional


Observations / Clarifying Questions / Insights:
- time taken to complete all task == time taken to complete the longest pair of tasks
    - reduce the max of all pairs
- the smallest max of all pairs >= the max number


- simplest / smallest problem
	-

- If I knew / had this....
	- the smallest max of all pairs
	- reverse this statement

Output: list of pairs
- optimal assignment of tasks for each worker, such that the tasks are completed as fast as possible.
- where each pair, stores the indices of the tasks that should be completed by one worker
    - [task_1, task_2] or [task_2, task_1]
-
'''

'''
Algo Time: O() | # Space: O():
Main Function
repeat while len of output array < len of input array
    sum all pairing possibilities
    for each num, find smallest max
    find smallest max of all smallest maxes
    append indices to output array

    - Input: int k, array tasks
		- create task_assignment, max_sum_array, max_sum_idx_array
        - create while loop that will run while len(task_assignment) < len(tasks)
            - loop over each idx that is not in task_assignment
                - loop over each pair_idx that is not in task_assignment
                    - sum idx_value and pair_value
                    - if sum value and pair_value > max at idx
                        - update max at idx in the max_sum_array
                        - update indices at idx in the max_sum_idx_array
            - find indices that equal the max in the max_sum_array
                - append to task_assignment

        Base case:
            -
        -
        -
    - Output: array task_assignment
		- task_assignment
'''

# Time: O(n^4) | # Space: O(n)


def taskAssignment_nnnn(k, tasks):
    task_assignment, max_sum_array = [], []
    max_sum_idx_dict = {}
    for idx in range(len(tasks)):
        max_sum_array.append(-1)
        max_sum_idx_dict[idx] = -1

    while len(task_assignment) < k:
        for i in range(len(tasks)):
            found_idx = False
            for ii in range(len(task_assignment)):
                idx1 = task_assignment[ii][0]
                idx2 = task_assignment[ii][1]
                if i == idx1 or i == idx2:
                    found_idx = True
            if found_idx is True:
                continue

            num = tasks[i]

            for ii in range(len(tasks)):
                if ii == i:
                    continue
                found_idx = False
                for iii in range(len(task_assignment)):
                    idx1 = task_assignment[iii][0]
                    idx2 = task_assignment[iii][1]
                    if ii == idx1 or ii == idx2:
                        found_idx = True
                if found_idx is True:
                    continue

                pair_num = tasks[ii]
                sum = num + pair_num

                if sum > max_sum_array[i]:
                    max_sum_array[i] = sum
                    max_sum_idx_dict[i] = ii

        smallest_max = float('inf')
        for i in range(len(max_sum_array)):

            found_idx = False
            for ii in range(len(task_assignment)):
                idx1 = task_assignment[ii][0]
                idx2 = task_assignment[ii][1]
                if i == idx1 or i == idx2:
                    found_idx = True

            if found_idx is True:
                continue

            max = max_sum_array[i]
            if max < smallest_max:
                smallest_max = max
                smallest_max_idx = i

        idx1 = smallest_max_idx
        idx2 = max_sum_idx_dict[smallest_max_idx]
        assignment = (idx1, idx2)
        task_assignment.append(assignment)

        for i in range(len(max_sum_array)):
            found_idx = False
            for ii in range(len(task_assignment)):
                idx1 = task_assignment[ii][0]
                idx2 = task_assignment[ii][1]
                if i == idx1 or i == idx2:
                    found_idx = True

            if found_idx is True:
                continue

            max_sum_array[i] = -1
            max_sum_idx_dict[i] = -1

    return task_assignment

# Time: O() | # Space: O()


def taskAssignment(k, tasks):
    # Write your code here.
    return []


k = 3
tasks = [1, 3, 5, 3, 1, 4]
print("k:", k)
print("tasks:", tasks)
print("taskAssignment_nnnn:", taskAssignment_nnnn(k, tasks))
print("taskAssignment:", taskAssignment(k, tasks))
print(" ")
'''
k = 7
tasks = [2, 1, 3, 4, 5, 13, 12, 9, 11, 10, 6, 7, 14, 8]
print("k:", k)
print("tasks:", tasks)
print("taskAssignment_nnnn:", taskAssignment_nnnn(k, tasks))
print("taskAssignment:", taskAssignment(k, tasks))
print(" ")

k = 3
tasks = [87, 65, 43, 32, 31, 320]
print("k:", k)
print("tasks:", tasks)
print("taskAssignment_nnnn:", taskAssignment_nnnn(k, tasks))
print("taskAssignment:", taskAssignment(k, tasks))
print(" ")

# _recursion
# _iteration
print(" ")
'''
