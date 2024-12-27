import math

def knightConnection(knightA, knightB):
    possibleMoves = [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]

    queue = [[knightA[0], knightA[1], 0]]
    visited = {positionToString(knightA)}

    while True:
        currentPosition = queue.pop(0)

        foundKnightB = currentPosition[0] == knightB[0] and currentPosition[1] == knightB[1]
        if foundKnightB:
            return math.ceil(currentPosition[2] / 2)


        for possibleMove in possibleMoves:
            newPosition = [currentPosition[0] + possibleMove[0], currentPosition[1] + possibleMove[1]]
            newPositionString = positionToString(newPosition)

            if newPositionString not in visited:
                newPosition.append(currentPosition[2] + 1)
                queue.append(newPosition)
                visited.add(newPositionString)

def positionToString(position):
    return ",".join(map(str, position))