import graphics.dda
import multiprocessing as mp
from graphics.point_storer import PointStorer
import random
import time


ps = PointStorer()
random.seed(50)

for i in range(50):
    x = random.randint(-1000, 1000)
    y = random.randint(-1000, 1000)

    ps.add((x,y))

print(ps.numPoints)
items = []

with mp.Pool(12) as pool:
    for idx in range(1, len(ps.points["x"])):
        p1 = (ps.points["x"][idx-1], ps.points["y"][idx-1])
        p2 = (ps.points["x"][idx], ps.points["y"][idx])
        items.append([p1, p2])
    print("START PROCESSING")

    start = time.time()
    results = pool.starmap(graphics.dda.dda2d, items)
    finish = time.time()

    print(f"Parallel = {finish-start}")

res = []
for idx in range(1, len(ps.points["x"])):
    p1 = (ps.points["x"][idx-1], ps.points["y"][idx-1])
    p2 = (ps.points["x"][idx], ps.points["y"][idx])
    res.append([p1,p2])

resultados = []
start =time.time()
for p1, p2 in res:
    resultados.append(graphics.dda.dda2d(p1,p2))
finish = time.time()

print(f"Sequencial = {finish-start}")
