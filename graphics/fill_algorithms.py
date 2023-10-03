from typing import Tuple, List


def boundaryFill(graph, startPoint: Tuple[int, int], fillColor: str, boundaryColors: List):
    x, y = startPoint
    graph.DrawPoint((x, y), 1, color=str)

    # if color x + 1, y not in boundaryColors