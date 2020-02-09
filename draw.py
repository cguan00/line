from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0


    x = x0
    y = y0

    a = (y1 - y)
    b = -1 * (x1 - x)

    if x < x1:
        m = -1 * float(a) / float(b) #slope
        #octant 1 and 5
        if m <= 1 and m >= 0:
            d = (2 * a) + b
            while x <= x1:
                plot(screen, color, x, y)
                if d > 0:
                    y += 1
                    d += 2 * b
                x += 1
                d += 2 * a
        #octant 2 and 6
        elif m > 1:
            d = a + (2 * b)
            while y <= y1:
                plot(screen, color, x, y)
                if d < 0:
                    x += 1
                    d += 2 * a
                y += 1
                d += 2 * b
        #octant 8 and 4
        elif m <= 0 and m >= -1:
            d = (2 * a) + b
            while x <= x1:
                plot(screen, color, x, y)
                if d < 0:
                    y -= 1
                    d -= 2 * b
                x += 1
                d += 2 * a
        #octant 7 and 3
        if m <= -1:
            d = a - (2 * b)
            while y >= y1:
                plot (screen, color, x, y)
                if d > 0:
                    x += 1
                    d += 2 * a
                y -= 1
                d -= 2 * b

    else: # vertical line
        if y < y1:
            while y < y1:
                plot(screen, color, x, y)
                y += 1
        else:
            while y > y1:
                plot(screen, color, x, y)
                y -= 1
