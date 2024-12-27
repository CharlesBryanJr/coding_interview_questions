def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def prove_fibonacci_sum(n):
    if n < 0:
        return "Invalid input. n must be a non-negative integer."

    # Base case
    if n == 0:
        return 0 == (fibonacci(0) + fibonacci(1)) - 1

    # Inductive step
    sum_of_fibonacci = 0
    for i in range(n + 1):
        sum_of_fibonacci += fibonacci(i)

    fibonacci_result = fibonacci(n + 2) - 1

    return sum_of_fibonacci == fibonacci_result


# Test the proof for various values of n
for n in range(10):
    print(f"n = {n}: {prove_fibonacci_sum(n)}")