from graphics import graphics_utils, translation
from graphics.point_storer import PointStorer

def shear2d(figure: PointStorer, **kwargs) -> PointStorer:
    axis        = kwargs.get("axis", None)
    shearFactor = kwargs.get("factor", None)

    new_figure = graphics_utils.move_to_origin(figure.copy())

    if axis in ["x", "both"]:
        for idx, (x, y) in enumerate(zip(new_figure.points["x"], new_figure.points["y"])):
            new_figure.points["x"][idx] = x + shearFactor * y

    if axis in ["y", "both"]:
        for idx, (x, y) in enumerate(zip(new_figure.points["x"], new_figure.points["y"])):
            new_figure.points["y"][idx] = y + shearFactor * x
        
    new_figure  = translation.translation2d(new_figure, axis="x", x_padding=figure.points["x"][0])
    new_figure  = translation.translation2d(new_figure, axis="y", y_padding=figure.points["y"][0])

    return new_figure