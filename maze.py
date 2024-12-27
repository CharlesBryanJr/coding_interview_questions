'''maze.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
print(" ")

from os import listdir
from os.path import isfile
import time
from queue import Queue


def read_in_out():
    """
    My automated tester! Just goes through all the .in and .out files 
    in the current directory and checks output/expected output
    """

    print("* Testing Maze Problem *")

    onlyFiles = [f for f in listdir() if f.split(".")[-1] != "py" and isfile(f)]
    count = 0
    cases = 0
    wrong = 0
    timeOut = 0
    
    results = []
    while count < len(onlyFiles):
        cases+= 1
        inp = open(onlyFiles[count], "r").readlines()
        out = open(onlyFiles[count+1], "r").readlines()
        _in = [x.strip() for x in inp]
        _out = [x.strip() for x in out]

        start = time.time()
        ans = run(_in)

        if ans == _out:
            print("Found in " + str(time.time() - start)[:5] + "ms", end=" | ")
            print("CORRECT")
            results.append("# ")
        elif ans == None:
            timeOut += 1
            print("TIMEOUT")
            results.append("T ")
        else:
            wrong += 1
            print("Found in " + str(time.time() - start)[:5] + "ms", end=" | ")
            print("INCORRECT")
            print("Excpected: ")
            print(_out)
            print("Your Answer: ")
            print(ans)
            results.append("_")

        count += 2

    # OUTPUT RESULTS
    print("***** Results *****")
    print("Problems: " + str(cases))
    print("Correct: " + str(cases-wrong-timeOut))
    print("Timed Out: " + str(timeOut))
    print("Incorrect: " + str(wrong))
    print("Score: " + str(cases-wrong-timeOut) + "/" + str(cases))
    print(*results)
    print("* DONE Testing Maze Problem *")


class Node:
    #Node class, simply stores neighboring nodes of a node
    def __init__(self, neighbors):
        """
        neighbors are stored as ints *NOT <code>Node</code>'s*
        """
        self.neighbors = neighbors

    def __str__(self):
        return str(self.neighbors)


def run(inp):
    # Basic principle here is I have a dict that stores all my Node objects
    # when I want a nodes neighbors I use the node number or id as a key to access it's neighbors.
    # For the BFS I simply store lists containing the current path, so the last number in the list
    # will be the current node (ie the one that neighbors need to be explored next),
    # when the last node is the same as the first node in the list we have
    # achieved the goal. 

    # key i is node i
    maze = {}  # dict to store nodes

    # Split the input into two parts
    info = inp[1:int(inp[0])+1]  
    start_rooms = inp[int(inp[0])+2:] # these are all of the start rooms

    start = time.time() # so we can timeout

    # Convert each line of input into a list full of ints
    for i in range(1, len(info)+1):
        formatLine = list(map(lambda x: int(x), info[i-1].strip().split(" ")[1:]))
        maze[i] = Node(formatLine)

    # Stores the answers
    out = []
    for room in start_rooms: # have to loop for each room asked of us
        room = int(room)
        mx = 0  # current max value

        # Simple FIFO Queue
        q = Queue()
        for n in maze[room].neighbors:
            q.put([room,n]) # Start the queue with each of the starting room nodes

        while not q.empty():  # BFS!

            # just timeout after 0.5 seconds
            if time.time() - start > 0.5:
                return None

            current = q.get()  # dequeue

            if current[-1] == room: # if we end up back in the same room
                if len(current) > mx:
                    mx = len(current)
            else:
                new = current[:]  # copy the current path

                # check if the current node has only one neighbor
                if len(maze[current[-1]].neighbors) == 1: 
                    new.append(maze[current[-1]].neighbors[0])
                else:
                    # here we are going to determine which neighbor we go to next, we have to go clockwise because of
                    # the problem specifications

                    # find what hallway we came through
                    last_pos = maze[current[-1]].neighbors.index(current[-2]) 

                    
                    # if the hallway we came through was the last in the
                    # neighbor list (so most clockwise?) just go back to the first hall
                    # were just trying to figure out what hall to chose next
                    if last_pos + 1 >= len(maze[current[-1]].neighbors):
                        last_pos = -1                                     
                                                                          

                    # add one to the last position and add that as next node
                    add = maze[current[-1]].neighbors[last_pos + 1]  
                    new.append(add)

                # if the last element is the room we started in
                if new[-1] == room:  
                    if len(current)+1 > mx:
                        mx = len(current) + 1
                else:
                    q.put(new)  # add new path to check

        out.append(str(mx-1))

    return out


read_in_out()

print(" ")