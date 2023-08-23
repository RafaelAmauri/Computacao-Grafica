from graphics import graphics_utils, translation
from graphics.point_storer import PointStorer


def scale2d(figure: list, **kwargs):
    axis    = kwargs.get("axis", None)
    x_scale = kwargs.get("x_scale", None)
    y_scale = kwargs.get("y_scale", None)

    new_figure = PointStorer()
    for pX, pY in zip(figure.points["x"], figure.points["y"]):
        new_figure.add((pX, pY))

    new_figure = graphics_utils.move_to_origin(new_figure)

    if axis in ["x", "both"]:
        new_figure.points["x"] = [x*x_scale for x in new_figure.points["x"]]

    if axis in ["y", "both"]:
        new_figure.points["y"] = [y*y_scale for y in new_figure.points["y"]]


    new_figure = translation.translation2d(new_figure, axis="x", x_padding=figure.points["x"][0])
    new_figure = translation.translation2d(new_figure, axis="y", y_padding=figure.points["y"][0])

    return new_figure