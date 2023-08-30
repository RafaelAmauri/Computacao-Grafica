import random
from graphics.point_storer import PointStorer
from graphics import dda
from graphics import bresenham
import time

random.seed(50)
ddapoints= PointStorer()
bres = PointStorer()

num_elements = 10000
for i in range(num_elements):
    x = random.randint(0,600)
    y = random.randint(0,600)
    ddapoints.add((x,y))
    bres.add((x,y))


start = time.time()
for idx in range(1, num_elements):
    previousx = ddapoints.points["x"][idx-1]
    previousy = ddapoints.points["y"][idx-1]
    currentx = ddapoints.points["x"][idx]
    currenty = ddapoints.points["y"][idx]

    ddares = dda.dda2d((previousx,previousy), (currentx, currenty))

finish = time.time()
print(f"DDA = {finish-start}")

start=time.time()
for idx in range(1, num_elements):
    previousx = ddapoints.points["x"][idx-1]
    previousy = ddapoints.points["y"][idx-1]
    currentx = ddapoints.points["x"][idx]
    currenty = ddapoints.points["y"][idx]

    bresres = bresenham.bresenham2d((previousx,previousy), (currentx, currenty))


finish = time.time()
print(f"Bresenham = {finish-start}")