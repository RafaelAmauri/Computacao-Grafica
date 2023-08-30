from graphics.point_storer import PointStorer


# Abstraction to make it easier to call the function
def drawLineBresenham(graph, point1: tuple, point2: tuple, color: str):
    if point1 == point2:
        return

    for x, y in bresenham2d(point1=point1, point2=point2):
        
        graph.DrawPoint((x, y),
                        4,
                        color=color
                        )


# Retuns the points between point1 and point2
def bresenham2d(point1: tuple, point2: tuple) -> PointStorer:
    p1X, p1Y = point1
    p2X, p2Y = point2

    deltaX = int(p2X - p1X)
    deltaY = int(p2Y - p1Y)

    bresenhamPoints = PointStorer()

    incrementX = 1 if deltaX >= 0 else -1
    incrementY = 1 if deltaY >= 0 else -1

    deltaX = abs(deltaX)
    deltaY = abs(deltaY)

    
    tempX, tempY = point1
    bresenhamPoints.add((tempX,tempY))

    # 1 caso
    if deltaX > deltaY:
        p  = 2 * deltaY - deltaX
        c1 = 2 * deltaY
        c2 = 2 * (deltaY - deltaX)

        for _ in range(deltaX):
            if p < 0:
                p += c1
            else:
                p += c2
                tempY += incrementY
            
            tempX += incrementX
            bresenhamPoints.add((tempX,tempY))
    
    # 2 caso
    else:
        p  = 2 * deltaX - deltaY
        c1 = 2 * deltaX
        c2 = 2 * (deltaX - deltaY)

        for _ in range(deltaY):
            if p < 0:
                p += c1
            else:
                p += c2
                tempX += incrementX

            tempY += incrementY
            bresenhamPoints.add((tempX,tempY))
    
    return bresenhamPoints