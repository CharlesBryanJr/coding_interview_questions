'''file_name'''
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

Type of Question:
-

Clarifying Questions / Insights:
-

Edge cases:
-

Base case:
-

Question:
- In a theater, an usher guides you to a row
where you can choose any empty seat.
- You want a seat that offers the most space
while being centrally positioned. 
- The theater row is represented as an array of integers,
where 1s denote occupied seats and 0s denote empty seats.
- You must find the optimal seat index to sit in,
considering that someone occupies the first and last seats.
- If two seats have the same optimal conditions,
choose the one with the lower index.
- If no seat is available, return -1.
- The input array will always contain at least one element
and consist only of 1s and 0s.

If I knew the ranges of available seats
'''

'''
Algo Time: O() | # Space: O():
-
-
    - Input: (seats)
        - find the available seats
        - for each available seat,
	    how many open spaces do I have to the left and right?
	    - check which seat is the lower idx
    - Output: best_seat_idx (int)
'''

# _recursion
# _iteration

# Time: O() | # Space: O()
def bestSeat_iteration(seats):
    best_seat = - 1
    most_space = float('-inf')

    i = 0
    in_range = i < len(seats)
    while in_range:
        available_seat = (seats[i] == 0)
        if available_seat:
            start = i
            while available_seat and in_range:
                i += 1
                in_range = i < len(seats)
                available_seat = (seats[i] == 0)
            end = i - 1
            space_count = end - start
            if space_count > most_space:
                best_seat = (start + end) // 2
                most_space = space_count
        else:
            i += 1
            in_range = i < len(seats)
            continue

    return best_seat


def bestSeat_recursion(seats):
    start_idx, start, end = 0, 0, 0
    best_seat = -1
    most_space = 0
    return find_best_seat(start_idx, start, end, most_space, best_seat, seats)

def find_best_seat(i, start, end, most_space, best_seat, seats):
    in_range = i < len(seats)
    if not in_range:
        return best_seat

    available_seat = (seats[i] == 0)
    if available_seat:
        return find_best_seat(i + 1, start, i, most_space, best_seat, seats)

    if end - start > most_space:
        best_seat = (end + start) // 2
        most_space = end - start

    return find_best_seat(i + 1, i + 1, i + 1, most_space, best_seat, seats)

seats = [1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1]
print("seats:", seats)
print("bestSeat_iteration:", bestSeat_iteration(seats))
print("bestSeat_recursion:", bestSeat_recursion(seats))
print(" ")

seats = [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1]
print("seats:", seats)
print("bestSeat_iteration:", bestSeat_iteration(seats))
print("bestSeat_recursion:", bestSeat_recursion(seats))
print(" ")

seats = [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1]
print("seats:", seats)
print("bestSeat_iteration:", bestSeat_iteration(seats))
print("bestSeat_recursion:", bestSeat_recursion(seats))
print(" ")
