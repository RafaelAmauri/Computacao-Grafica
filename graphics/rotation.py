import math
from graphics import graphics_utils
from graphics import translation


def rotation2d(figure: list, **kwargs):
    direction = kwargs.get("direction", None)
    angle     = kwargs.get("angle", None)
    angle     = angle * math.pi / 180

    new_figure = figure.copy()
    new_figure = interface_utils.move_to_origin(new_figure)

    new_x = []
    new_y = []

    if direction == "clockwise":
        for x, y in zip(new_figure["x"], new_figure["y"]):
            new_x.append(round( x * math.cos(angle) + y * math.sin(angle), 4))
            new_y.append(round(-x * math.sin(angle) + y * math.cos(angle), 4))
    else:
        for x, y in zip(new_figure["x"], new_figure["y"]):
            new_x.append(round(x * math.cos(angle) - y * math.sin(angle), 4))
            new_y.append(round(x * math.sin(angle) + y * math.cos(angle), 4))
        
    new_figure["x"] = new_x
    new_figure["y"] = new_y

    new_figure  = translation.translation2d(new_figure, axis="x", x_padding=figure["x"][0])
    new_figure  = translation.translation2d(new_figure, axis="y", y_padding=figure["y"][0])

    return new_figure