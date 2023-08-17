from graphics import graphics_utils, translation

def shear2d(figure: list, **kwargs):
    # https://www.javatpoint.com/computer-graphics-shearing

    axis        = kwargs.get("axis", None)
    shearFactor = kwargs.get("factor", None)

    new_figure = graphics_utils.move_to_origin(figure.copy())

    if axis in ["x", "both"]:
        for idx, (x, y) in enumerate(zip(new_figure["x"], new_figure["y"])):
            new_figure["x"][idx] = x + shearFactor * y

    if axis in ["y", "both"]:
        for idx, (x, y) in enumerate(zip(new_figure["x"], new_figure["y"])):
            new_figure["y"][idx] = y + shearFactor * x
        
    new_figure  = translation.translation2d(new_figure, axis="x", x_padding=figure["x"][0])
    new_figure  = translation.translation2d(new_figure, axis="y", y_padding=figure["y"][0])

    return new_figure