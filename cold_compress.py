'''cold_compress.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
print(" ")

# GET INPUT FROM LINE
'''
n = int(input())
lines = []

for _ in range(n):
    lines.append(input())'''

# GET INPUT FROM TEXT FILE
with open("cold_compress_input.txt", "r") as f:
    lines = f.readlines()

print(lines)
# SOLVE PROBLEM

for line in lines[1:]: # For each input
    line = line.strip() # Remove \n from line
    
    newStr = ""
    last = line[0]
    count = 1

    for char in line[1:]: # For every character except the first (because we already handled it above)
        
        if char == last: # If the next character is equal to the last (consecutive chars)
            count += 1
        else: # If the next character is different
            newStr += str(count) + " " + last + " "
            count = 1
            last = char
            
    newStr += str(count) + " " + last
    print(newStr)


print(" ")