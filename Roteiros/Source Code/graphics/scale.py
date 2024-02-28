from graphics import translation
from graphics.point_storer import PointStorer
from utils import graphics_utils


def scale2d(figure: PointStorer, **kwargs):
    axis    = kwargs.get("axis", None)
    scaleFactor = kwargs.get("factor", None)

    new_figure = graphics_utils.move_to_origin(figure.copy())

    if axis in ["x", "both"]:
        new_figure.points["x"] = [x*scaleFactor for x in new_figure.points["x"]]

    if axis in ["y", "both"]:
        new_figure.points["y"] = [y*scaleFactor for y in new_figure.points["y"]]


    new_figure = translation.translation2d(new_figure, axis="x", factor=figure.points["x"][0])
    new_figure = translation.translation2d(new_figure, axis="y", factor=figure.points["y"][0])

    return new_figure