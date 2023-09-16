from typing import Tuple

'''
Calcultates the code for a given point in (X,Y)
'''
def calculateCodeCohenSutherland(x: int, 
                                y: int, 
                                xLimits: Tuple[int, int], 
                                yLimits: Tuple[int, int]
                                ) -> int:

    xmin, xmax = xLimits
    ymin, ymax = yLimits

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


'''
Applies the Cohen-Sutherland algorithm to a line, denoted by <startPoint> and <endPoint>

Input: 
    - startPoint: the first point in the line
    - endPoint:   the last point in the line
    - xLimits:    a tuple with the minimum and maximum values for the X axis
    - yLimits:    a tuple with the minimum and maximum values for the Y axis

Returns:
    - isAccepted: a bool telling whether or not the line is accepted
    - (startPoint, endPoint): the new starting and ending points. If the line 
    is already inside the bounds estipulated by x/yLimits, these won't change.
    Always check isAccepted before rendering the line to not accidentaly
    render a line that's completely outside bounds.
'''
def cohenSutherland(startPoint: Tuple[int, int], 
                    endPoint: Tuple[int, int], 
                    xLimits: Tuple[int, int], 
                    yLimits: Tuple[int, int]
                    ) -> Tuple[bool, Tuple[Tuple[int, int], Tuple[int, int]]]:
    print("COHEN")
    # Define variables we'll be working with
    x1, y1 = startPoint
    x2, y2 = endPoint
    
    xmin, xmax = xLimits
    ymin, ymax = yLimits

    LEFT   = 1
    RIGHT  = 2
    BOTTOM = 4
    TOP    = 8

    isAccepted = False

    outcode1 = calculateCodeCohenSutherland(x1, y1, xLimits, yLimits)
    outcode2 = calculateCodeCohenSutherland(x2, y2, xLimits, yLimits)

    print(f"Outcode1 = {outcode1}")
    print(f"Outcode2 = {outcode2}")

    while True:
        # The line is fully inside bounds
        if (outcode1 == 0) and (outcode2 == 0):
            isAccepted = True
            break

        # The line is fully outside bounds
        elif (outcode1 != 0) and (outcode2 != 0):
            break

        # Only part of the line is outside bounds.
        else:
            # Figure out which of the endpoints triggered this
            outcodeOut = outcode1 if outcode1 != 0 else outcode2

            # Find intersection points.
            if outcodeOut & TOP:
                newX = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
                newY = ymax
            elif outcodeOut & BOTTOM:
                newX = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
                newY = ymin
            elif outcodeOut & RIGHT:
                newY = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
                newX = xmax
            elif outcodeOut & LEFT:
                newY = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
                newX = xmin
            
            # If it's startPoint that's out of bounds, readjust it
            if outcodeOut == outcode1:
                x1 = newX
                y1 = newY
                outcode1 = calculateCodeCohenSutherland(x1, y1, xLimits, yLimits)
            # Otherwise, it's endPoint
            else:
                x2 = newX
                y2 = newY
                outcode2 = calculateCodeCohenSutherland(x2, y2, xLimits, yLimits)

    clippedStartPoint = (x1, y1)
    clippedEndPoint   = (x2, y2)

    return isAccepted, (clippedStartPoint, clippedEndPoint)



'''
To be used by liangBarsky
'''
def clipTest(p: int, q: int, t1: int, t2: int) -> bool:
    result = True

    # Entry point
    if p < 0:
        r = q / p
        # Line is outside the clipping edge!
        if r > t2:
            result = False
        elif r > t1:
            t1 = r
    
    else:
        if p > 0:
            r = q / p
            
            if r < t1:
                result = False
            elif r < t2:
                t2 = r
        
        else:
            if q < 0:
                result = False
    

    return result, t1, t2


'''
Applies the Liang-Barsky algorithm to a line, denoted by <startPoint> and <endPoint>

Input: 
    - startPoint: the first point in the line
    - endPoint:   the last point in the line
    - xLimits:    a tuple with the minimum and maximum values for the X axis
    - yLimits:    a tuple with the minimum and maximum values for the Y axis

Returns:
    - isAccepted: a bool telling whether or not the line should be rendered
    - (startPoint, endPoint): the new starting and ending points. If the line 
    is already inside the bounds estipulated by x/yLimits, these won't change.
    
    Always check isAccepted before rendering the line to not accidentaly
    render a line that's completely outside bounds!
'''
def liangBarsky(startPoint: Tuple[int, int], 
                endPoint: Tuple[int, int], 
                xLimits: Tuple[int, int], 
                yLimits: Tuple[int, int]
                ) -> Tuple[bool, Tuple[Tuple[int, int], Tuple[int, int]]]:

    print("LIANG BARSKY")
    x1, y1 = startPoint
    x2, y2 = endPoint
    
    xmin, xmax = xLimits
    ymin, ymax = yLimits

    deltaX = x2 - x1
    deltaY = y2 - y1


    t1 = 0
    t2 = 1

    # This looks awful, but it's either this or a huge if statement.
    # At least this way we can have a more compact comparison
    clause1, t1, t2 = clipTest(-deltaX, x1 - xmin, t1, t2)
    clause2, t1, t2 = clipTest(deltaX, xmax - x1, t1, t2)
    clause3, t1, t2 = clipTest(-deltaY, y1 - ymin, t1, t2)
    clause4, t1, t2 = clipTest(deltaY, ymax - y1, t1, t2)

    if clause1 and clause2 and clause3 and clause4:
        if t2 < 1:
            x2 = int( x1 + (t2*deltaX) )
            y2 = int( y1 + (t2*deltaY) )

        if t1 > 0:
            x1 = int( x1 + (t1*deltaX) )
            y1 = int( y1 + (t1*deltaY) )


        clippedStartPoint = (x1, y1)
        clippedEndPoint   = (x2, y2)

        return True, (clippedStartPoint, clippedEndPoint)
    
    return False, (clippedStartPoint, clippedEndPoint)
