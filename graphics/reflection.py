from graphics import graphics_utils, translation
from graphics.point_storer import PointStorer


def reflection2d(figure: list, **kwargs):
    axis    = kwargs.get("axis", None)

    new_figure = graphics_utils.move_to_origin(figure.copy())

    if axis in ["x", "both"]:
        new_figure.points["x"] = [x*-1 for x in new_figure.points["x"]]

    if axis in ["y", "both"]:
        new_figure.points["y"] = [y*-1 for y in new_figure.points["y"]]

    new_figure  = translation.translation2d(new_figure, axis="x", x_padding=figure.points["x"][0])
    new_figure  = translation.translation2d(new_figure, axis="y", y_padding=figure.points["y"][0])

    return new_figure