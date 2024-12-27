'''nth_fib'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0621
# pylint: disable=W0102
print(" ")

# F(n) = F(n-1) + F(n-2)
# F(1) = 0
# F(2) = 1
# given n, return the nth Fibonacci number


# Time: O(n) | # Space: O(n)
def getNthFib_n_n(n):
    fib_sequence = [0, 1]
    if n in fib_sequence:
        return 0
    for i in range(2, n):
        new_fib_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(new_fib_num)
    return fib_sequence[-1]

# Time: O(n) | # Space: O(n)
def getNthFib_n_n_recursion(n):
    fib_sequence = [0, 1]
    if n in fib_sequence:
        return 0
    return get_nth_fib_n_n(2, n, fib_sequence)


def get_nth_fib_n_n(i, n, fib_sequence):
    out_of_range = i >= n
    if out_of_range:
        return fib_sequence[-1]
    new_fib_num = fib_sequence[-1] + fib_sequence[-2]
    fib_sequence.append(new_fib_num)
    return get_nth_fib_n_n(i + 1, n, fib_sequence)


# Time: O(n) | # Space: O(1)
def getNthFib_n_1(n):
    fib_sequence = [0, 1]
    if n in fib_sequence:
        return 0
    for i in range(2, n):
        new_fib_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence[-2] = fib_sequence[-1]
        fib_sequence[-1] = new_fib_num
    return fib_sequence[-1]

def getNthFib_n_1_recursion(n):
    fib_sequence = [0, 1]
    if n in fib_sequence:
        return 0
    return get_nth_fib_n_1(2, n, fib_sequence)

def get_nth_fib_n_1(i, n, fib_sequence):
    out_of_range = i >= n
    if out_of_range:
        return fib_sequence[-1]
    new_fib_num = fib_sequence[-1] + fib_sequence[-2]
    fib_sequence[-2] = fib_sequence[-1]
    fib_sequence[-1] = new_fib_num
    return get_nth_fib_n_1(i + 1, n, fib_sequence)


n = 6
print(" ")
print("Time: O(n) | # Space: O(n): ", getNthFib_n_n(n))
print(" ")
print("Time: O(n) | # Space: O(n): ", getNthFib_n_n_recursion(n))
print(" ")
print("# Time: O(n) | # Space: O(1): ", getNthFib_n_1(n))
print(" ")
print("# Time: O(n) | # Space: O(1): ", getNthFib_n_1_recursion(n))
print(" ")