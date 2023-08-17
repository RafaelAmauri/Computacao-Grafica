def translation2d(figure: list, **kwargs):
    axis      = kwargs.get("axis", None)
    x_padding = kwargs.get("x_padding", None)
    y_padding = kwargs.get("y_padding", None)

    if axis in ["x", "ambos"]:
        figure["x"] = [x+x_padding for x in figure["x"]]
    if axis in ["y", "ambos"]:
        figure["y"] = [y+y_padding for y in figure["y"]]

    return figure