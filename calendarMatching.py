'''calendarMatching.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
# pylint: disable=C0304
# pylint: disable=C0200
print(" ")

'''

Question:
The calendar matching question asks us to,
schedule a meeting with a co worker for a certain duration.

We have visibility to both,
our own calendar and our co worker's calendar.
	each calendar contains the,
	start time and end time of each meeting,
	for the given day you want to schedule the meeting on

We also have visibility to both,
	meeting participants,
	earliest time and latest time,
	they are willing to meet.

Given the above,
and the duration,
of the meeting you would like to schedule,
return a list of "time blocks",
	[start time and end time]
that the meeting could occur during.


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

# Dictionaries (Hashmaps)
 # Understand how to add addition values to a key in a dictionary
    # for each key, create the values as a 2D array
    # when addition values need to be added to a key, append the addition values
	# Understand how to avoid duplicates
    # only add a key & value to a dictionary
    # at the last occurence/opportunity to create the key & value
    # or
    # add to a key's values in a dictionary
    # at the last occurence/opportunity to add to the key's values


Input(matrix, array, matrix, array, int): calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration
# Intuitive
# Primitive Types
		# Strings
			# Empty string
			# NULL or nil (and Optionals, depending on language)
			# Spaces (multiple words or sentences, or single/multiple whitespaces alone)
			# Punctuation
			# Upper, lowercase, or mixed (e.g., “stRiNg”)
			# Strings of numbers (e.g., “12”) Should these be changed to Int, Float, or Double?
			# Different Languages (Diacritics? Unicode compliant? ASCII?)
			# Emoji 👍 (especially if question is presented as a text field input by a user)
			# Long String
		# Arrays
			# Empty array
			# Nested or not nested
		# Dictionaries (Hashmaps)
			# Collisions

Observations / Clarifying Questions / Insights:
# military time
# the calendars will be sorted by start time in ascending order 


Output(matrix): time_blocks
time_blocks will represent the times that the meeting to schedule, can occur
[start time and end time]
'''


# Time: O(n + m) | # Space: O(n + m)
def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    updated_calendar1 = update_calendar(calendar1, dailyBounds1)
    updated_calendar2 = update_calendar(calendar2, dailyBounds2)
    merged_calendars = merge_calendars(updated_calendar1, updated_calendar2)
    flattened_calendar = flatten_calendar(merged_calendars)
    return get_available_meeting_slots(flattened_calendar, meetingDuration)

def update_calendar(calendar, dailyBounds):
    updated_calendar = calendar[:]
    updated_calendar.insert(0, ["0:00", dailyBounds[0]])
    updated_calendar.append([dailyBounds[1], "23:59"])
    return list(map(lambda m: [time_to_minutes(m[0]), time_to_minutes(m[1])], updated_calendar))

def time_to_minutes(time):
    hours, minutes = list(map(int, time.split(":")))
    return hours * 60 + minutes

def merge_calendars(calendar1, calendar2):
    merged_calendar = []
    i = 0
    j = 0
    while i < len(calendar1) and j < len(calendar2):
        meeting1 = calendar1[i]
        meeting2 = calendar2[j]
        if meeting1[0] <= meeting2[0]:
            merged_calendar.append(meeting1)
            i += 1
        else:
            merged_calendar.append(meeting2)
            j += 1
    while i < len(calendar1):
        merged_calendar.append(meeting1)
        i += 1
    while j < len(calendar2):
        merged_calendar.append(meeting2)
        j += 1

    return merged_calendar

def flatten_calendar(calendar):
    flattened_calendar = [calendar[0][:]]
    for i in range(1, len(calendar)):
        current_meeting = calendar[i]
        previous_meeting = flattened_calendar[-1]
        current_start, current_end = current_meeting
        previous_start, previous_end = previous_meeting

        if previous_end >= current_start:
            new_previous_meeting = [previous_start, max(previous_end, current_end)]
            flattened_calendar[-1] = new_previous_meeting
        else:
            flattened_calendar.append(current_meeting[:])
    return flattened_calendar

def get_available_meeting_slots(calendar, meetingDuration):
    meeting_slots = []
    for idx in range(1, len(calendar)):
        start = calendar[idx - 1][1]
        end = calendar[idx][0]
        slot_duration = end - start
        if slot_duration >= meetingDuration:
            meeting_slots.append([start, end])
    return list(map(lambda m: [minutes_to_time(m[0]), minutes_to_time(m[1])], meeting_slots))

def minutes_to_time(minutes):
    hours = minutes // 60
    hours_string = str(hours)
    mins = minutes % 60
    mins_string = "0" + str(mins) if mins < 10 else str(mins)
    return hours_string + ":" + mins_string

calendar1 = [
    ["9:00", "10:30"],
    ["12:00", "13:00"],
    ["16:00", "18:00"]
]
dailyBounds1 = ["9:00", "20:00"]
calendar2 = [
    ["10:00", "11:30"],
    ["12:30", "14:30"],
    ["14:30", "15:00"],
    ["16:00", "17:00"]
]
dailyBounds2 = ["10:00", "18:30"]
meetingDuration = 30

print("calendar1:", calendar1)
print("dailyBounds1:", dailyBounds1)
print("calendar2:", calendar2)
print("dailyBounds2:", dailyBounds2)
print("meetingDuration:", meetingDuration)
print("calendarMatching:", calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration))
print(" ")

calendar1 = []
dailyBounds1 = ["9:30", "16:30"]
calendar2 = []
dailyBounds2 = ["10:00", "18:30"]
meetingDuration = 60

print("calendar1:", calendar1)
print("dailyBounds1:", dailyBounds1)
print("calendar2:", calendar2)
print("dailyBounds2:", dailyBounds2)
print("meetingDuration:", meetingDuration)
print("calendarMatching:", calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration))
print(" ")

calendar1 = [
    ["7:00", "7:45"],
    ["8:15", "8:30"],
    ["9:00", "10:30"],
    ["12:00", "14:00"],
    ["14:00", "15:00"],
    ["15:15", "15:30"],
    ["16:30", "18:30"],
    ["20:00", "21:00"]
]
dailyBounds1 = ["6:30", "22:00"]
calendar2 = [
    ["9:00", "10:00"],
    ["11:15", "11:30"],
    ["11:45", "17:00"],
    ["17:30", "19:00"],
    ["20:00", "22:15"]
]
dailyBounds2 = ["8:00", "22:30"]
meetingDuration = 30

print("calendar1:", calendar1)
print("dailyBounds1:", dailyBounds1)
print("calendar2:", calendar2)
print("dailyBounds2:", dailyBounds2)
print("meetingDuration:", meetingDuration)
print("calendarMatching:", calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration))
print(" ")

# _recursion
# _iteration
print(" ")
