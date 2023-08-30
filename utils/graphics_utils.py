from graphics import translation
from graphics.point_storer import PointStorer


# Sets a figure's starting position to (0,0). Please, make sure the first point is the one 
# closest to (0,0) and also make sure that the point's coordinates are equals. Example: (2,2), (3,3), (100,100), etc
def move_to_origin(figure:PointStorer) -> PointStorer:
    new_figure = figure.copy()

    new_figure = translation.translation2d(new_figure, axis="x", factor=new_figure.points["x"][0] * -1)
    new_figure = translation.translation2d(new_figure, axis="y", factor=new_figure.points["y"][0] * -1)
    
    return new_figure