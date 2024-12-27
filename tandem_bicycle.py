'''tandem_bicycle.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
print(" ")

# faster pedaler determine the speed of the bicycle

# given two same length arrays of postive integers
# pair integers with the largest differences together and then increment the speed with the max or min 

def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    team_size = len(redShirtSpeeds)
    max_speed = 0
    min_speed = 0
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort(reverse=True)

    print(redShirtSpeeds)
    print(blueShirtSpeeds)

    if fastest is True:
        for idx in range(team_size):
            print(max(redShirtSpeeds[idx], blueShirtSpeeds[idx]))
            max_speed += max(redShirtSpeeds[idx], blueShirtSpeeds[idx])
        
        return max_speed

    else:
        for idx in range(team_size):
            blueShirtSpeeds.sort()
            print(max(redShirtSpeeds[idx], blueShirtSpeeds[idx]))
            min_speed += max(redShirtSpeeds[idx], blueShirtSpeeds[idx])
        
        return min_speed

redShirtSpeeds = [5, 5, 3, 9, 2]
blueShirtSpeeds = [3, 6, 7, 2, 1]
fastest = False
print("Speed:",tandemBicycle(redShirtSpeeds,blueShirtSpeeds,fastest))

print(" ")
