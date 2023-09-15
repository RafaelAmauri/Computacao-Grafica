

def calculateCode(x: int, y: int, xmin: int, xmax: int, ymin: int, ymax: int) -> int:
    code = 0

    if x < xmin:
        code |= 1  # Set the least significant bit (bit 0) to 1
    if x > xmax:
        code |= 2  # Set the second least significant bit (bit 1) to 1
    if y < ymin:
        code |= 4  # Set the third least significant bit (bit 2) to 1
    if y > ymax:
        code |= 8  # Set the fourth least significant bit (bit 3) to 1

    return code


def cohenSutherland(point1: tuple, point2: tuple, xmin: int, xmax: int, ymin: int, ymax: int) -> tuple:
    x1, y1 = point1
    x2, y2 = point2
    
    TOP    = 8
    BOTTOM = 4
    RIGHT  = 2
    LEFT   = 1

    isAccepted = False

    outcode1 = calculateCode(x1, y1, xmin, xmax, ymin, ymax)
    outcode2 = calculateCode(x2, y2, xmin, xmax, ymin, ymax)

    while True:

        # Line is fully inside bounds
        if outcode1 == 0 and outcode2 == 0:
            isAccepted = True
            break

        # Line is fully outside bounds
        elif outcode1 != 0 and outcode2 != 0:
            break
        
        # Partially inside bounds.
        else:
            # Figure out what endpoint is outside bounds
            outcodeOut = outcode1 if outcode1 != 0 else outcode2

            # Find intersection points.
            if outcodeOut & TOP:
                x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
                y = ymax
            elif outcodeOut & BOTTOM:
                x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
                y = ymin
            elif outcodeOut & RIGHT:
                y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
                x = xmax
            elif outcodeOut & LEFT:
                y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
                x = xmin
            
            # If it's <point1> that's out of bounds, readjust it
            if outcodeOut == outcode1:
                x1 = x
                y1 = y
                outcode1 = calculateCode(x1, y1, xmin, xmax, ymin, ymax)
            # Otherwise, it's <point2>
            else:
                x2 = x
                y2 = y
                outcode1 = calculateCode(x2, y2, xmin, xmax, ymin, ymax)


    point1 = (x1, y1)
    point2 = (x2, y2)
    return (point1, point2)