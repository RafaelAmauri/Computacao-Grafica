from typing import Tuple, List, Dict
from graphics.line_algorithms import bresenham2d
from graphics.point_storer import PointStorer


'''
Applies the boundary fill algorithm to paint an area in the graph
Fill order = Up -> Right -> Below -> Left

Input:
    - graph: the PySimpleGUI Graph element
    - startPoint: the starting point for the algorithm
    - userPoints: list of the points filled up by the user
    - userUsedColors: list of the colors the user used
    - fillColor: the color that will be used to color the area
    - canvas limit: the limit size of the canvas

Returns:
    - None
'''
def boundaryFill(graph, startPoint: Tuple[int, int], userPoints: PointStorer, userUsedColors: List, fillColor: str, canvasSize) -> None:
    coloredPoints = dict()
    canvasSizeX, canvasSizeY = canvasSize
    
    print("Boundary Fill!")

    # Iterating over all points in userPoints and calculating intermediates with bresenham. Since we can't access
    # the image buffer with TK, we need to build our own representation of what is in the image. In short, this is a dict that
    # stores all points that were modified and what their color is. If an (x, y) point is not in the dict, it means its color
    # is the default, white.
    previousX = userPoints.points["x"][0]
    previousY = userPoints.points["y"][0]
    # idx because we need to access userUsedColors too
    for idx in range(1, userPoints.numPoints):
        currentX = userPoints.points["x"][idx]
        currentY = userPoints.points["y"][idx]
        
        for intermediateX, intermediateY in bresenham2d(startPoint=(previousX, previousY), endPoint=(currentX, currentY)):
            coloredPoints[f"{intermediateX}, {intermediateY}"] = userUsedColors[idx]
            
        # Update for the next loop
        previousX = currentX
        previousY = currentY
    

    # Add starting point to the stack
    stack = [startPoint]
    while stack:
        x, y = stack.pop()

        try:
            colorPixel = coloredPoints[f"{x}, {y}"]
        except KeyError:
            colorPixel = None

        if (
            -canvasSizeX <= x <= canvasSizeX
            and -canvasSizeY <= y <= canvasSizeY
            and colorPixel not in userUsedColors
            and colorPixel != fillColor
        ): 
            graph.DrawPoint((x, y), 10, color=fillColor)
            coloredPoints[f"{x}, {y}"] = fillColor
            print(f"Filling {x}, {y}")

            # Add neighbors to the stack
            stack.append((x, y+1))
            stack.append((x+1, y))
            stack.append((x, y-1))
            stack.append((x-1, y))



'''
Applies the flood fill algorithm to paint an area in the graph
Fill order = Up -> Right -> Below -> Left

Input:
    - graph: the PySimpleGUI Graph element
    - startPoint: the starting point for the algorithm
    - userPoints: list of the points filled up by the user
    - userUsedColors: list of the colors the user used
    - fillColor: the color that will be used to color the area
    - canvas limit: the limit size of the canvas

Returns:
    - None
'''
def floodFill(graph, startPoint: Tuple[int, int], userPoints: PointStorer, userUsedColors: List, fillColor: str, canvasSize: Tuple[int, int]):
    coloredPoints = dict()
    canvasSizeX, canvasSizeY = canvasSize

    print("Flood Fill!")

    # Iterating over all points in userPoints and calculating intermediates with bresenham. Since we can't access
    # the image buffer with TK, we need to build our own representation of what is in the image. In short, this is a dict that
    # stores all points that were modified and what their color is. If an (x, y) point is not in the dict, it means its color
    # is the default, white.
    previousX = userPoints.points["x"][0]
    previousY = userPoints.points["y"][0]
    # idx because we need to access userUsedColors too
    for idx in range(1, userPoints.numPoints):
        currentX = userPoints.points["x"][idx]
        currentY = userPoints.points["y"][idx]
        
        for intermediateX, intermediateY in bresenham2d(startPoint=(previousX, previousY), endPoint=(currentX, currentY)):
            coloredPoints[f"{intermediateX}, {intermediateY}"] = userUsedColors[idx]
            
        # Update for the next loop
        previousX = currentX
        previousY = currentY
    

    x, y = startPoint
    try:
        startColor = coloredPoints[f"{x}, {y}"]
    except KeyError:
        startColor = None


    # Add starting point to the stack
    stack = [startPoint]
    while stack:
        x, y = stack.pop()

        try:
            colorPixel = coloredPoints[f"{x}, {y}"]
        except KeyError:
            colorPixel = None

        if (
            -canvasSizeX <= x <= canvasSizeX
            and -canvasSizeY <= y <= canvasSizeY
            and startColor == colorPixel
        ): 
            graph.DrawPoint((x, y), 10, color=fillColor)
            coloredPoints[f"{x}, {y}"] = fillColor
            print(f"Filling {x}, {y}")

            # Add neighbors to the stack
            stack.append((x, y+1))
            stack.append((x+1, y))
            stack.append((x, y-1))
            stack.append((x-1, y))