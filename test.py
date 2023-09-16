from graphics.clipping_algorithms import cohenSutherland, liangBarsky


point1 = (-222, -78)
point2 = (138, 208)
xLimits = (0,  200)
yLimits = (0, 200)
accepted, (rP1, rP2) = cohenSutherland(point1, point2, xLimits, yLimits)
print(accepted)
print(rP1)
print(rP2)

point1 = (-222, -78)
point2 = (138, 208)
xLimits = (0,  200)
yLimits = (0, 200)
accepted, (rP1, rP2) = liangBarsky(point1, point2, xLimits, yLimits)
print(accepted)
print(rP1)
print(rP2)