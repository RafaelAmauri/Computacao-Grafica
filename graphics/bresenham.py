from graphics.point_storer import PointStorer


def bresenham2d(point1: tuple, point2: tuple) -> PointStorer:
    p1X, p1Y = point1
    p2X, p2Y = point2

    deltaX = p2X - p1X
    deltaY = p2Y - p1Y

    if deltaX > deltaY: 
        p = 2 * deltaY - deltaX
        c1 = 2 * deltaY
        c2 = 2* (deltaX - deltaY)