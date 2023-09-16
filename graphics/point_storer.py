'''
This class was created by me to suit the needs for a way to store the points in a quick way as well
as providing fast and efficient lookup times.

The reason this exists is because programming languages don't have a builtin structure 
that provides O(1) times for lookup and insertion while maintaining the order of the insertions.

The order in which the user inserts the points is crucial for calculating the starting and ending points
when drawing a line. We can't lose track of that, so the natural implementation calls for a list. 
But the problem with lists is that when we want to see if a point is already inserted to avoid duplicates, 
we have to loop through the entire list to find if it exists, giving us O(N) time.

This PointStorer class that I made solves this problem, providing O(1) insertion and lookup times with standard
Python types while also maintaining insertion order.
'''


class PointStorer:
    def __init__(self) -> None:
        # Where we store all the points the user has drawn on the canvas.
        self.points = {
            "x": [],
            "y": []
        }

        # Used as a validation measure to stop the user from adding two
        # duplicate points, while providing O(1) lookup and write times
        self.val = set()

        self.numPoints = 0
        self.currentIndex = 0


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

    
    def copy(self):
        return self.__copy__()

    
    def __contains__(self, item):
        return item in self.val


    def __copy__(self):
        newPoints = PointStorer()

        for px, py in zip(self.points["x"], self.points["y"]):
            newPoints.points["x"].append(px)
            newPoints.points["y"].append(py)
        
        newPoints.val = self.val
        newPoints.numPoints = self.numPoints

        return newPoints


    def __iter__(self):
        self.currentIndex = 0
        return self


    def __next__(self):
        try:
            v = (self.points["x"][self.currentIndex], self.points["y"][self.currentIndex])
        except IndexError:
            raise StopIteration()
        
        self.currentIndex += 1
        return v