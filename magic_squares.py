'''magic_squares.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=C0303
import math

print(" ")

sqaure1 = [2, 2, 2, 
           2, 2, 2, 
           2, 2, 2 ]

sqaure2 = [16, 2, 3, 13,
           5, 11, 10, 8, 
           9, 7, 6, 12, 
           4, 14, 15, 1 ]

sqaure3 = [2, 7, 6,
           9, 5, 1, 
           4, 3, 8 ]

def is_square_magic(sqaure):

    count_to_n = 0
    row_sum = 0
    column_sum = 0
    count_to_n = 0
    magic_total = 0
    
    for num in range(1,1000):
        if (len(sqaure) / num) == 1:
            n = int(math.sqrt(num))
            break

    for num in sqaure:
        if count_to_n == n:
            break
        
        magic_total += num
        count_to_n += 1

    count_to_n = 0
    for num in sqaure:
        if count_to_n == n:
            if row_sum != magic_total or column_sum != magic_total:
                return False
            
            row_sum, column_sum, count_to_n = 0, 0, 0

        row_sum += num
        column_sum += num
        count_to_n += 1
    
    print("n:", n)
    print("magic_total:", magic_total)
    return True



print(is_square_magic(sqaure1))
print("---")
print("---")
print("---")
print(is_square_magic(sqaure2))
print("---")
print("---")
print("---")
print(is_square_magic(sqaure3))
print(" ")