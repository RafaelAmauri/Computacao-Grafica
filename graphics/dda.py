import math

def dda2d(point1: tuple, point2: tuple):
    p1X, p1Y = point1
    p2X, p2Y = point2

    deltaX = int(p2X - p1X)
    deltaY = int(p2Y - p1Y)

    pointsInLine = {
        "x": [],
        "y": []
    }

    # A função round do python estava arredondando 2.5 pra 2 ao invés de 3, então
    # fiz meu próprio round
    roundDDA = lambda n: float(math.ceil(n)) if n%1 >= 0.5 else float(math.floor(n))

    # TODO O sinal de deltaX e deltaY está zoando a conta
    # X aumenta de 1 em 1, Y aumenta de acordo com <increment>
    if deltaX > deltaY:
        increment = deltaY / deltaX

        pointsInLine["x"] = [p1X + step for step in range(abs(deltaX)+1)] if deltaX > 0 else [p1X - step for step in range(abs(deltaX)+1)]

        yant = increment + p1Y
        pointsInLine["y"].append(p1Y)
        extendY = [roundDDA(yant + increment*step) for step in range(abs(deltaY+1))] if deltaY > 0 else [roundDDA(yant - increment*step) for step in range(abs(deltaY)+1)]
        pointsInLine["y"].extend(extendY)

    # Y aumenta de 1 em 1, X aumenta de acordo com <increment>
    else:
        increment = deltaX / deltaY

        pointsInLine["y"] = [p1Y + step for step in range(deltaY+1)]

        xant = increment + p1X
        pointsInLine["x"].append(p1X)
        pointsInLine["x"].extend([roundDDA(xant + increment * step) for step in range(deltaX+1)])

    return pointsInLine