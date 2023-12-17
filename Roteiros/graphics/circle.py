import math
from graphics.point_storer import PointStorer


def circle2d(origin, resolution, radius) -> PointStorer():
    selectedX, selectedY = origin

    pi = math.pi
    circlePoints = PointStorer()

    for point in range(0, resolution+1):
        circlePoints.add(((math.cos(2*pi / resolution*point) * radius) + selectedX, (math.sin(2*pi / resolution*point) * radius) + selectedY))

    return circlePoints