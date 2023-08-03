import matplotlib.pyplot as plt
import translation, utils


def scale2d(figure: list, **kwargs):
    axis    = kwargs.get("axis", None)
    x_scale = kwargs.get("x_scale", None)
    y_scale = kwargs.get("y_scale", None)

    new_figure = figure.copy()

    new_figure = utils.move_to_origin(new_figure)
    
    if axis in ["x", "both"]:
        if x_scale > 1:
            new_figure["x"] = [x*x_scale for x in new_figure["x"]]
        else:
            new_figure["x"] = [x*x_scale for x in new_figure["x"]]

        new_figure  = translation.translation2d(new_figure, axis="x", x_padding=figure["x"][0])


    if axis in ["y", "both"]:
        if y_scale > 1:
            new_figure["y"] = [y*y_scale for y in new_figure["y"]]
        else:
            new_figure["y"] = [y*y_scale for y in new_figure["y"]]

        new_figure = translation.translation2d(new_figure, axis="y", y_padding=figure["y"][0])
    

    return new_figure