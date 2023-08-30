from graphics import translation
from graphics.point_storer import PointStorer
from utils import graphics_utils


def reflection2d(figure: PointStorer, **kwargs):
    axis = kwargs.get("axis", None)

    new_figure = figure.copy()

    if axis in ["x", "both"]:
        new_figure.points["x"] = [x*-1 for x in new_figure.points["x"]]

    if axis in ["y", "both"]:
        new_figure.points["y"] = [y*-1 for y in new_figure.points["y"]]

    return new_figure