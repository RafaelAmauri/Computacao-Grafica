from graphics.point_storer import PointStorer


def translation2d(figure: PointStorer(), **kwargs) -> PointStorer:
    axis      = kwargs.get("axis", None)
    x_padding = kwargs.get("x_padding", None)
    y_padding = kwargs.get("y_padding", None)

    new_figure = figure.copy()

    if axis in ["x", "both"]:
        new_figure.points["x"] = [x+x_padding for x in figure.points["x"]]
    if axis in ["y", "both"]:
        new_figure.points["y"] = [y+y_padding for y in figure.points["y"]]

    return new_figure