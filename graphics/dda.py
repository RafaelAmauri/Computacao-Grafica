import math

def dda2d(point1: tuple, point2: tuple):
    p1X, p1Y = point1
    p2X, p2Y = point2

    deltaX = int(p2X - p1X)
    deltaY = int(p2Y - p1Y)

    ddaPoints = {
        "x": [],
        "y": []
    }

    # Python's default round function is not working. It's rounding 2.5 to 2 instead of 3, so
    # I decided to make my own
    roundDDA = lambda n: float(math.ceil(n)) if n%1 >= 0.5 else float(math.floor(n))

    nSteps = abs(deltaX) if abs(deltaX) > abs(deltaY) else abs(deltaY)
    
    incrementX = float(deltaX/nSteps) if deltaX != 0 else 0
    incrementY = float(deltaY/nSteps) if deltaY != 0 else 0
    
    tempX = p1X
    tempY = p1Y
    for _ in range(nSteps+1):
        tempX += incrementX
        tempY += incrementY

        ddaPoints["x"].append(roundDDA(tempX))
        ddaPoints["y"].append(roundDDA(tempY))

    return ddaPoints