import math

from typing import Tuple
from graphics.point_storer import PointStorer


'''
It's an abstraction to make it easier to call bresenham2d() and dda2d().

This function takes all the points returned by bresenham2d()/dda2d()
and draws each of these points on a PySimpleGUI Graph.

Input: 
    - graph:      the PySimpleGUI Graph element that we'll be drawing on
    - startPoint: the starting point
    - endPoint:   the last point
    - color:      the color the line will be drawn in
'''
def drawLineBresenham(   graph,
                        startPoint: Tuple[int, int], 
                        endPoint: Tuple[int, int], 
                        color: str) -> None:
    
    if startPoint == endPoint:
        return

    for x, y in bresenham2d(startPoint, endPoint):
        graph.DrawPoint((x, y),
                        4,
                        color=color
                        )


'''
Applies the Bresenham algorithm to return the points between two endpoints

Input: 
    - startPoint: the starting point
    - endPoint:   the last point

Returns:
    - bresenhamPoints: a PointStorer object(check graphics/point_storer.py if you don't know
    what that is) with all the points between startPoint and endPoint.
'''
def bresenham2d(startPoint: Tuple[int, int], 
                endPoint: Tuple[int, int]
                ) -> PointStorer:

    x1, y1 = startPoint
    x2, y2 = endPoint

    deltaX = int(x2 - x1)
    deltaY = int(y2 - y1)

    bresenhamPoints = PointStorer()

    incrementX = 1 if deltaX >= 0 else -1
    incrementY = 1 if deltaY >= 0 else -1

    deltaX = abs(deltaX)
    deltaY = abs(deltaY)

    
    tempX, tempY = startPoint
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


'''
Python's math.round() function rounds all floats to the nearest even number.
So for example, round(2.5) is 2 instead of 3, so I decided to make my own
rounding function
'''
def roundDDA(n):
    return math.ceil(n) if n%1 >= 0.5 else math.floor(n)


'''
It's an abstraction to make it easier to call dda2d().

This function takes all the points returned by dda2d()
and draws each of these points on a PySimpleGUI Graph.

Input: 
    - graph:      the PySimpleGUI Graph element that we'll be drawing on
    - startPoint: the starting point
    - endPoint:   the last point
    - color:      the color the line will be drawn in
'''
def drawLineDDA(    graph,
                    startPoint: Tuple[int, int], 
                    endPoint: Tuple[int, int], 
                    color: str) -> None:
    
    if startPoint == endPoint:
        return

    for x, y in dda2d(startPoint, endPoint):
        graph.DrawPoint((x, y),
                        4,
                        color=color
                        )


'''
Applies the DDA algorithm to return the points between two endpoints

Input: 
    - startPoint: the starting point
    - endPoint:   the last point

Returns:
    - ddaPoints: a PointStorer object(check graphics/point_storer.py if you don't know
    what that is) with all the points between startPoint and endPoint.
'''
def dda2d(  startPoint: Tuple[int, int], 
            endPoint: Tuple[int, int]
            ) -> PointStorer:

    x1, y1 = startPoint
    x2, y2 = endPoint

    deltaX = int(x2 - x1)
    deltaY = int(y2 - y1)

    ddaPoints = PointStorer()

    nSteps = abs(deltaX) if abs(deltaX) > abs(deltaY) else abs(deltaY)
    
    incrementX = deltaX/nSteps if deltaX != 0 else 0
    incrementY = deltaY/nSteps if deltaY != 0 else 0
    
    tempX = x1
    tempY = y1
    for _ in range(nSteps+1):
        tempX += incrementX
        tempY += incrementY

        ddaPoints.add((roundDDA(tempX), roundDDA(tempY)))

    return ddaPoints