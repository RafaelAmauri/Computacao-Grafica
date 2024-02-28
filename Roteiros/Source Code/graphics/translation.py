from graphics.point_storer import PointStorer


def translation2d(figure: PointStorer(), **kwargs) -> PointStorer:
    axis = kwargs.get("axis", None)
    translationFactor = kwargs.get("factor", None)

    new_figure = figure.copy()

    if axis in ["x", "both"]:
        new_figure.points["x"] = [x+translationFactor for x in figure.points["x"]]
    if axis in ["y", "both"]:
        new_figure.points["y"] = [y+translationFactor for y in figure.points["y"]]

    return new_figure