'''class_photos.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=C0200
print(" ")

# even number of students
# half of the students are wearing red shirts
# half of the students are wearing blue shirts
# arange the students into two rows
# length of row 1 == length of row 2
# one row must contain only students in red shirts
# one row must contain only student in blue shirts
# students in row 2 must be taller than the student in row 1 directly infront of them
# each class has atlest two students

# given two same length arrays of postive integers 
# return True or False

redShirtHeights = [5, 8, 1, 3, 4]
blueShirtHeights = [6, 9, 2, 4, 5]

def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()
    arange_count = 0

    print(redShirtHeights)
    print(blueShirtHeights)


    for i in range(len(redShirtHeights)):
        
        if redShirtHeights[i] > blueShirtHeights[i]:
            arange_count += 1
        
    if arange_count == len(redShirtHeights):
        return True

    arange_count = 0
    for i in range(len(blueShirtHeights)):
        
        if blueShirtHeights[i] > redShirtHeights[i]:
            arange_count += 1
        
    if arange_count == len(blueShirtHeights):
        return True
    
    return False



print(classPhotos(redShirtHeights, blueShirtHeights))

print(" ")