def countSquares(points):
    pointsSet = set()
    for point in points:
        pointsSet.add(pointToString(point))

    count = 0
    for pointA in points:
        for pointB in points:
            if pointA == pointB:
                continue

            midPoint_X = (pointA[0] + pointB[0]) / 2
            midPoint_Y = (pointA[1] + pointB[1]) / 2

            xDistanceFromMidPoint = pointA[0] - midPoint_X
            yDistanceFromMidPoint = pointA[1] - midPoint_Y

            pointC = [midPoint_X + yDistanceFromMidPoint, midPoint_Y - xDistanceFromMidPoint]
            pointD = [midPoint_X - yDistanceFromMidPoint, midPoint_Y + xDistanceFromMidPoint]

            found_square = pointToString(pointC) in pointsSet and pointToString(pointD) in pointsSet
            if found_square:
                count += 1

    return count / 4

def pointToString(point):
    notWholeNumber = point[0] % 1 == 0 and point[1] % 1 == 0
    if notWholeNumber:
        point = [int(coordinate) for coordinate in point]
    return '.'.join([str(coordinate) for coordinate in point])