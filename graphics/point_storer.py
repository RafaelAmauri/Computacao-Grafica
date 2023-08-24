# This class was created to suit the needs for a way to store the points in a quick way as well
# as providing fast and efficient lookup times.

# The driving factor for implementing this was because we had a O(N) lookup time. 
# When the user adds a new point to the canvas, it requires checking if it's already there
# or we end up with duplicates. This verification required looping through the whole list of points 
# and checking if it's already there, which gives us O(N) complexity.

# Changing the way we store points to a set also wouldn't work, as it needs to be ordered. When drawing the lines for a new point
# we need to get the coordinates for the last one to maintain the shape of the object.

# This class was imagined as a way to provide the best of both worlds. We store the elements in memory on a list to keep it ordered, but when looking
# up if an element is already inserted we now can have this operation O(1) time. This implementations takes advantage of Python sets for this.
# Under the hood the Python set uses a hashmap for lookups and avoid duplicates. The hashmap is one of the more powerful data structures, providing
# O(1) lookup and write times, and now we can use these too.


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
            p = (self.points["x"][self.currentIndex], self.points["y"][self.currentIndex])
        except IndexError:
            raise StopIteration()
        
        self.currentIndex += 1
        return p