import math
from graphics import graphics_utils, translation
from graphics.point_storer import PointStorer


def rotation2d(figure: PointStorer, **kwargs):
    direction = kwargs.get("direction", None)
    angle     = kwargs.get("angle", None)
    angle     = angle * math.pi / 180

    new_figure = PointStorer()
    new_figure = graphics_utils.move_to_origin(figure)

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

    new_figure  = translation.translation2d(new_figure, axis="x", x_padding=figure.points["x"][0])
    new_figure  = translation.translation2d(new_figure, axis="y", y_padding=figure.points["y"][0])

    return new_figure