import matplotlib.pyplot as plt
from graphics import translation


# Displays a figure with its coordinates labeled. Nothing too fancy
def show_figure(original_figure: dict, new_figure:dict=None):
    plt.ylim(bottom=-50, top=50)
    plt.xlim(left=-50, right=50)


    plt.plot(original_figure["x"], original_figure["y"], 'ro-')
    for i_x, i_y in zip(original_figure["x"], original_figure["y"]):
        plt.text(i_x, i_y, f"{i_x}, {i_y}")

    if new_figure != None:
        plt.plot(new_figure["x"], new_figure["y"], 'bo--')
        for i_x, i_y in zip(new_figure["x"], new_figure["y"]):
            plt.text(i_x, i_y, f"{i_x}, {i_y}")

    plt.show()
    plt.clf()


# Sets a figure's starting position to (0,0). Please, make sure the first point is the one 
# closest to (0,0) and also make sure that the point's coordinates are equals. Example: (2,2), (3,3), (100,100), etc
def move_to_origin(figure:dict):
    new_figure = figure.copy()
    new_figure = translation.translation2d(new_figure, axis="x", x_padding=new_figure["x"][0]*-1)
    new_figure = translation.translation2d(new_figure, axis="y", y_padding=new_figure["y"][0]*-1)
    return new_figure