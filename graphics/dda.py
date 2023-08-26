import math
from graphics.point_storer import PointStorer

# Python by nature will round all floats to the nearest even number.
# So for example, round(2.5) is 2 instead of 3, so I decided to make my own
# rounding function
def roundDDA(n):
    return math.ceil(n) if n%1 >= 0.5 else math.floor(n)


def dda2d(point1: tuple, point2: tuple) -> PointStorer:
    p1X, p1Y = point1
    p2X, p2Y = point2

    if point1 == point2:
        return PointStorer()

    deltaX = int(p2X - p1X)
    deltaY = int(p2Y - p1Y)

    ddaPoints = PointStorer()

    nSteps = abs(deltaX) if abs(deltaX) > abs(deltaY) else abs(deltaY)
    
    incrementX = deltaX/nSteps if deltaX != 0 else 0
    incrementY = deltaY/nSteps if deltaY != 0 else 0
    
    tempX = p1X
    tempY = p1Y
    for _ in range(nSteps+1):
        tempX += incrementX
        tempY += incrementY

        ddaPoints.add((roundDDA(tempX), roundDDA(tempY)))

    return ddaPoints