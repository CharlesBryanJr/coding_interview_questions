def collatz(n):

    def recursion(x, iterations):
        print(f"{iterations}: {x}")

        if x in [0,1,2,4]:
            return x, iterations

        if x % 2 == 0:
            return recursion(x//2, iterations + 1)
        else:
            return recursion((x*3) + 1, iterations + 1)

    n, steps = recursion(n, 0)
    print(" ")
    print("n:", n)
    print("steps:",steps)

print(" ")
print("collatz(10):",collatz(10))
print(" ")