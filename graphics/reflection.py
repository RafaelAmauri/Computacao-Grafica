from graphics import graphics_utils
from graphics import translation

def reflection2d(figure: list, **kwargs):
    axis    = kwargs.get("axis", None)

    new_figure = figure.copy()
    new_figure = graphics_utils.move_to_origin(figure.copy())


    if axis in ["x", "both"]:
        new_figure["x"] = [x*-1 for x in new_figure["x"]]

    if axis in ["y", "both"]:
        new_figure["y"] = [y*-1 for y in new_figure["y"]]

    new_figure  = translation.translation2d(new_figure, axis="x", x_padding=figure["x"][0])
    new_figure  = translation.translation2d(new_figure, axis="y", y_padding=figure["y"][0])

    return new_figure