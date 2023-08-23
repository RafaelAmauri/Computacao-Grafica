class PointStorer:
    def __init__(self) -> None:
        # Where we store all the points the user has drawn on the canvas.
        self.points = {
            "x": [],
            "y": []
        }
        
        # val here is used an optimization of the code. As it stands, there is nothing stopping the
        # user from adding the same point multiple times. And checking if the point is already on a list
        # is not time-efficient as it requires looping through all the items on the list.

        # And since using a set to store the points doesn't work either because sets are unordered, we need
        # to have the points in a separate structure. Memory usage will be higher, but it is only storing two integers,
        # for each point, so while higher, it's still not very costly
        self.val = set()
        self.numPoints = 0


    def __contains__(self, item):
        return item in self.val


    def add(self, p: tuple):
        px, py = p
        
        self.points["x"].append(px)
        self.points["y"].append(py)

        self.val.add(p)

        self.numPoints += 1

    
    def clear(self):
        self.points["x"] = []
        self.points["y"] = []

        self.val = set()

        self.numPoints = 0