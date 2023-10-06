from typing import Tuple, List, Dict
from graphics.line_algorithms import bresenham2d
from graphics.point_storer import PointStorer

import sys
sys.setrecursionlimit(100000)

# Ordem de Prenchimento = Cima -> Direita -> Baixo -> Esquerda
def _boundaryFill(graph, startPoint: Tuple[int, int], modifiedPoints: Dict, fillColor: str, canvasLimits):
    stack = [startPoint]

    while stack:
        x, y = stack.pop()

        if (
            -canvasLimits <= x <= canvasLimits 
            and -canvasLimits <= y <= canvasLimits
            and f"{x}, {y}" not in modifiedPoints
        ): 
            graph.DrawPoint((x, y), 10, color=fillColor)
            modifiedPoints[f"{x}, {y}"] = fillColor
            print(f"Filling {x}, {y}")

            stack.append((x, y+1))
            stack.append((x+1, y))
            stack.append((x, y-1))
            stack.append((x-1, y))


def boundaryFill(graph, startPoint: Tuple[int, int], userPoints: List, userUsedColors: List, fillColor: str):
    modifiedPoints = dict()
    
    previousX = userPoints.points["x"][0]
    previousY = userPoints.points["y"][0]

    # idx because we need to access userUsedColors too
    for idx in range(1, userPoints.numPoints):
        currentX = userPoints.points["x"][idx]
        currentY = userPoints.points["y"][idx]
        
        for intermediateX, intermediateY in bresenham2d(startPoint=(previousX, previousY), endPoint=(currentX, currentY)):
            modifiedPoints[f"{intermediateX}, {intermediateY}"] = userUsedColors[idx]
            
        # Update for the next loop
        previousX = currentX
        previousY = currentY
    
    x, y = startPoint
    if f"{x}, {y}" not in modifiedPoints:
        modifiedPoints = _boundaryFill(graph, startPoint, modifiedPoints, fillColor, 600)