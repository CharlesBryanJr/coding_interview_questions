'''Hanoi'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0621
# pylint: disable=W0102
print(" ")


'''
- What: A precise specification of the problem that the algorithm solves.

- How: A precise description of the algorithm itself.

Hanoi


- Why: A proof that the algorithm solves the problem it is supposed to solve.

- How fast: An analysis of the running time of the algorithm.

note:
-
'''

def Hanoi(n, src, dst, tmp):
    if n > 0:
        Hanoi(n - 1, src, tmp, dst)
        print(f"move disk {n} from {src} to {dst}")
        Hanoi(n - 1, tmp, dst, src)


n = 3
print("n:", n)
print("Hanoi:", Hanoi(n, "a", "c", "b"))
print(" ")

n = 4
print("n:", n)
print("Hanoi:", Hanoi(n, "a", "c", "b"))
print(" ")

n = 5
print("n:", n)
print("Hanoi:", Hanoi(n, "a", "c", "b"))
print(" ")
