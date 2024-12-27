
'''apartmentHunting.py'''
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

Input():
# Intuitive
# Primitive Types
		# Numbers
			# Zero (0)
			# NULL or nil
			# Negative Numbers
			# Floats or Doubles (clarifies if Ints only?)
			# Min/Max Int
		# Arrays
			# Empty array
			# Nested or not nested
		# Dictionaries (Hashmaps)
			# Collisions

Output(int): idx
# index which represent the best apartment location
'''


# Time: O(b^2*r) | # Space: O(b)
def apartment_hunting_n_n(blocks, reqs):

    min_distance = float("inf")
    min_distance_idx = -1

    for i in range(len(blocks)):
        a = {}
        for req in reqs:
            a[req] = False

        distance = look(i, a, blocks)

        if distance < min_distance:
            min_distance = distance
            min_distance_idx = i

    return min_distance_idx


def look(i, a, blocks):
    left = i
    right = i

    max_distance = float("-inf")
    req_count = 0

    for distance in range(len(blocks)):
        left = i - distance
        right = i + distance

        if left >= 0:
            left_block = blocks[left]

            for building in left_block:

                if building not in a:
                    continue

                if left_block[building] is False:
                    continue

                if a[building] is True:
                    continue

                a[building] = True

                req_count += 1

                if distance > max_distance:
                    max_distance = distance

                if req_count == len(a):
                    return max_distance

        if right < len(blocks):
            right_block = blocks[right]

            for building in right_block:

                if building not in a:
                    continue

                if right_block[building] is False:
                    continue

                if a[building] is True:
                    continue

                a[building] = True

                req_count += 1

                if distance > max_distance:
                    max_distance = distance

                if req_count == len(a):
                    return max_distance

    return max_distance

'''
# Time: O(b^2*r) | # Space: O(b)
Main Function
Input(array, array): blocks, reqs

To solve the apartment hunting problem,
we need to figure out, which apartment is in the best location,
based on our need to go to an unknown amount of requirements.

location == idx
apartment == idx
requirementa == buildings that we need go to

Given a blocks hash table,
which details, 
which buildings are at which indices.

Given a reqs array,
which details, 
which buildings we would like to go to.

We need to find the best location/idx for an apartment,
that would allow us to go to every requirement,
in the smallest radius possible.

To solve this problem,
we will need to calculate, 
the distance between a given apartment/idx,
and furthest requirement.
    we need to find the furthest requirement,
    because, the furthest requirement,
    will be the maximum of the radius,
    that we need to travel,
    in order to visit each of our requirements

This calculatation will need to be repeated, 
for every apartment/idx.

For every apartment/idx,
we will need to loop thorugh the blocks,
and search for each requirement.
    Since, we will be walking,
    we want to know where the closest requirement.
        We wouldnt pass a closer requirement to go to a further one

    as we loop through the blocks,
    we will need to loop through requirements,
    and perform a constant time look up in the block,
    to check if the block "has",
    the current requirement,
    that we are looking for

        if so, we want calcuate the distance,
        we would have to walk/traverse to reach that requirement
        if the distance is closer than,
        the previous closest location,
        then, we have found,
        a closer location of the requirement,
        and we want to update,
        closet location distance for future iterations

        if not, continue

        once we have found the closest distance, 
        that we would have to walk/traverse, 
        to this requirment,
        we want to then compare,
        this distance to the furthest requirement,
            if the distance is further than,
            our current furthest requirement,
            then we would need to expand our radius,
            of how far we need to walk/traverse 
            to get to all of our requirements.
                again, our furthest requirement,
                determines our radius size,
                and all other requirements,
                will be at the same distance or closer

        at this point, 
        we have found the distance of,
        the furthest requirement,
        for this apartment/index
        now, 
        we need to add,
        the distance of the furthest requirement,
        to the furthest requirement array
            so that we can later compare,
            each indexs furthest requirement.

Once we have the furthest requirement, 
for each index,
we can compare each index to eachother,
and determine which location/idx for an apartment,
allows us to go to every requirement,
in the smallest radius possible.

the apartment/block/idx that has the,
closest furthest requirement,
is our best location.

Output(int): idx
# index which represent the best aparment location
'''

# Time: O(b^2*r) | # Space: O(b)
def apartment_hunting(blocks, reqs):
    furthest_requirement = []
    for idx in range(len(blocks)):
        furthest_requirement.append(float("-inf"))

    for apartment in range(len(blocks)):

        for req in reqs:
            closest_location = float("inf")

            for block in range(len(blocks)):

                if blocks[block][req] is True:

                    distance = abs(apartment - block)

                    closest_location = min(closest_location, distance)

            furthest_requirement[apartment] = max(furthest_requirement[apartment], closest_location)

    return get_idx_at_min_value(furthest_requirement)


def get_idx_at_min_value(array):
    min_value = float("inf")
    min_value_idx = None

    for idx in range(len(array)):
        value = array[idx]

        if value < min_value:
            min_value = value
            min_value_idx = idx

    return min_value_idx



'''
# Time: O(n * m) | # Space: O(n)
Main Function
Input(array, array): blocks, reqs

In this third and most optimal soultion,
we asked ourselves,
how can we improve our solution,
to run,
in a better time complexity.

In the previous solutions,
we needed three loops to calculate,
the best location for an apartment.

To improve the time completxity,
if we could reduce 3 loops down to 2 loops,
then we could dramatically improve our solution.

In this solution,
we asked and answered the question of,
if I knew or had this,
I could significantly,
simply the problem


If I knew / had this....
	For each location/idx,
    if I already knew,
    the distance to the, 
    closest location of each requirement

To precompute and store,
the distance to the closest location,
of a requirement,
we can run a loop from,
left to right, 0 to the end,
and then,
run a loop from
right to left, end to 0


    we will first check if the,
    req is located on this block/idx,
        if so, 
        update the "array",
        at the block/idx, to equal zero
            the requirment is on the,
            same block as the aparment
        
        update the variable,
        that stores the,
        location of, 
        the,
        last found requirment

        if not,
        calculate the absolute distance,
        from the block/idx, 
        to the last found location,
        of the requirment




Output(int): idx
# index which represent the best aparment location
'''

# Time: O(n * m) | # Space: O(n)
def apartmentHunting(blocks, reqs):
    a = list(map(lambda req: min_idx_distance_from_idx(req, blocks), reqs))
    return max_value_at_idx(a, blocks)

def min_idx_distance_from_idx(req, blocks):
    closest_req = []
    for idx in range(len(blocks)):
        closest_req.append(None)

    closest_req_idx = float('inf')

    for idx in range(len(blocks)):
        if blocks[idx][req] is True:
            closest_req_idx = idx

        distance = abs(idx - closest_req_idx)
        closest_req[idx] = distance

    closest_req_idx = float('inf')
    for idx in reversed(range(len(blocks))):
        if blocks[idx][req] is True:
            closest_req_idx = idx

        distance = abs(idx - closest_req_idx)
        closest_req[idx] = min(closest_req[idx], distance)

    return closest_req

def max_value_at_idx(array, blocks):
    min_radius = float("inf")
    min_radius_idx = None

    for i in range(len(blocks)):
        max_radius = float("-inf")
        for ii in range(len(array)):
            radius = array[ii][i]
            max_radius = max(max_radius, radius)

        if max_radius < min_radius:
            min_radius = max_radius
            min_radius_idx = i

    return min_radius_idx

blocks =[
    {
      "gym": False,
      "school": True,
      "store": False
    },
    {
      "gym": True,
      "school": False,
      "store": False
    },
    {
      "gym": True,
      "school": True,
      "store": False
    },
    {
      "gym": False,
      "school": True,
      "store": False
    },
    {
      "gym": False,
      "school": True,
      "store": True
    }
]
reqs = ["gym", "school", "store"]
print("blocks:", blocks)
print("reqs:", reqs)
print("apartment_hunting_n_n:", apartment_hunting_n_n(blocks, reqs))
print("apartment_hunting:", apartment_hunting(blocks, reqs))
print("apartmentHunting:", apartmentHunting(blocks, reqs))
print(" ")