import math
from graphics import translation
from graphics.point_storer import PointStorer
from utils import graphics_utils


def rotation2d(figure: PointStorer, **kwargs):
    direction = kwargs.get("direction", None)
    angle     = kwargs.get("angle", None)
    angle     = angle * math.pi / 180

    new_figure = graphics_utils.move_to_origin(figure.copy())

    new_x = []
    new_y = []

    if direction == "clockwise":
        for x, y in zip(new_figure.points["x"], new_figure.points["y"]):
            new_x.append(round( x * math.cos(angle) + y * math.sin(angle), 4))
            new_y.append(round(-x * math.sin(angle) + y * math.cos(angle), 4))
    else:
        for x, y in zip(new_figure.points["x"], new_figure.points["y"]):
            new_x.append(round(x * math.cos(angle) - y * math.sin(angle), 4))
            new_y.append(round(x * math.sin(angle) + y * math.cos(angle), 4))
        
    new_figure.points["x"] = new_x
    new_figure.points["y"] = new_y

    new_figure  = translation.translation2d(new_figure, axis="x", factor=figure.points["x"][0])
    new_figure  = translation.translation2d(new_figure, axis="y", factor=figure.points["y"][0])

    return new_figure