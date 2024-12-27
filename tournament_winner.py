'''tournament_winner.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
# pylint: disable=C0304
# pylint: disable=C0200

'''
Question:
# team compete against each other in a round robin
# home and away team
# [homeTeam, awayTeam]
# 1, home team won
# 0, away team won
# one winner and loser
# no ties
# winning team receives 3 points
# team name < 30 chars

Type of Question:
- Array
	- draw indices
	- sorting
    - multiple pointers
    - mutating the current index or later index to count
    - hashing the index values
		- running sums
		- sliding windows
			- start_of_window
			- end_of_window

Input:
- Intuitive
- Primitive Types
	- Strings
		- Empty string
		- NULL or nil (and Optionals, depending on language)
		- Spaces (multiple words or sentences, or single/multiple whitespaces alone)
		- Punctuation
		- Upper, lowercase, or mixed (e.g., “stRiNg”)
		- Strings of numbers (e.g., “12”) Should these be changed to Int, Float, or Double?
		- Different Languages (Diacritics? Unicode compliant? ASCII?)
		- Emoji 👍 (especially if question is presented as a text field input by a user)
		- Long String
'''

# Time: O(n) | # Space: O(k)
def tournamentWinner(competitions, results):
    tournament_winner_wins = 0
    winners = {}
    for idx in range(len(results)):
        winner = get_match_winner(idx, competitions, results)
        update_winners(winner, winners)
    return get_tournament_winner(tournament_winner_wins, winners)

def get_match_winner(idx, competitions, results):
    print(competitions[idx])
    if results[idx] == 0:
        winner = competitions[idx][1]
    else:
        winner = competitions[idx][0]
    return winner

def update_winners(winner, winners):
    if winner in winners:
        winners[winner] += 1
    else:
        winners[winner] = 1
    return None

def get_tournament_winner(tournament_winner_wins, winners):
    tournament_winner = ''
    for winner in winners:
        if winners[winner] > tournament_winner_wins:
            tournament_winner = winner
            tournament_winner_wins = winners[winner]
    return tournament_winner

# Test cases
competitions = [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"]
]
results = [0, 0, 1]
print("competitions:", competitions)
print("results:", results)
print("tournamentWinner:", tournamentWinner(competitions, results))
print(" ")

competitions = [
    ["HTML", "Java"],
    ["Java", "Python"],
    ["Python", "HTML"],
    ["C#", "Python"],
    ["Java", "C#"],
    ["C#", "HTML"],
    ["SQL", "C#"],
    ["HTML", "SQL"],
    ["SQL", "Python"],
    ["SQL", "Java"]
]
results = [0, 1, 1, 1, 0, 1, 0, 1, 1, 0]
print("competitions:", competitions)
print("results:", results)
print("tournamentWinner:", tournamentWinner(competitions, results))
print(" ")

competitions = [
    ["Bulls", "Eagles"],
    ["Bulls", "Bears"],
    ["Bears", "Eagles"]
]
results = [0, 0, 0]
print("competitions:", competitions)
print("results:", results)
print("tournamentWinner:", tournamentWinner(competitions, results))
print(" ")
