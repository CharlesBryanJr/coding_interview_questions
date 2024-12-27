'''stable_internships.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
# pylint: disable=C0304
print(" ")

'''

given:
- two 2D arrays of preferences data

action:
-

return:
- assgin 1 intern to each team
- 2D of each pairing of an intern to a team

note:
- assignment must be stable
    -
- tie breaker == intern's preference
-

'''

# Time: O(n^2) | # Space: O(n^2) 
def stableInternships(interns, teams):
    chosen_interns = {}
    free_interns = list(range(len(interns)))
    current_intern_choices = [0] * len(interns)
    
    team_maps = []
    for team in teams:
        rank = {}
        for i, intern_num in enumerate(team):
            rank[intern_num] = i
        team_maps.append(rank)
    
    while len(free_interns) > 0:
        intern_num = free_interns.pop()
        intern = interns[intern_num]

        team_pref = intern[current_intern_choices[intern_num]]
        current_intern_choxsices[intern_num] += 1
        
        if team_pref not in chosen_interns:
            chosen_interns[team_pref] = intern_num
            continue
        
        previous_intern = chosen_interns[team_pref]
        previous_intern_rank = team_maps[team_pref][previous_intern]
        current_intern_rank = team_maps[team_pref][intern_num]
        
        if current_intern_rank < previous_intern_rank:
            free_interns.append(previous_intern)
            chosen_interns[team_pref] = intern_num
        else:
            free_interns.append(intern_num) 
        
    matches = [[intern_num, team_num] for team_num, intern_num in chosen_interns.items()]                
    return matches

interns = [
    [0, 1, 2],
    [2, 1, 0],
    [1, 2, 0]
]
teams = [
    [2, 1, 0],
    [0, 1, 2],
    [0, 2, 1]
]
print("interns:", interns)
print("teams:", teams)
print("stableInternships:", stableInternships(interns, teams))
print(" ")

interns = [
    [0, 1, 2, 3],
    [0, 1, 3, 2],
    [0, 2, 3, 1],
    [0, 2, 3, 1]
]
teams = [
    [1, 3, 2, 0],
    [0, 1, 2, 3],
    [1, 2, 3, 0],
    [3, 0, 2, 1]
]
print("interns:", interns)
print("teams:", teams)
print("stableInternships:", stableInternships(interns, teams))
print(" ")

interns = [
    [1, 0],
    [0, 1]
]
teams = [
    [0, 1],
    [1, 0]
]
print("interns:", interns)
print("teams:", teams)
print("stableInternships:", stableInternships(interns, teams))
print(" ")

# _recursion
# _iteration
print(" ")
