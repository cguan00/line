from display import *
from draw import *
from random import seed
from random import randint

s = new_screen()
c = [ 0, 255, 0 ]

# #octants 1 and 5
# draw_line(0, 0, XRES-1, YRES-1, s, c)
# draw_line(0, 0, XRES-1, YRES / 2, s, c)
# draw_line(XRES-1, YRES-1, 0, 250, s, c)
#
# #octants 8 and 4
# c[BLUE] = 255;
# draw_line(0, YRES-1, XRES-1, 0, s, c);
# draw_line(0, YRES-1, XRES-1, YRES/2, s, c);
# draw_line(XRES-1, 0, 0, 250, s, c);
#
# #octants 2 and 6
# c[RED] = 255;
# c[GREEN] = 0;
# c[BLUE] = 0;
# draw_line(0, 0, XRES/2, YRES-1, s, c);
# draw_line(XRES-1, YRES-1, 250, 0, s, c);
#
# #octants 7 and 3
# c[BLUE] = 255;
# draw_line(0, YRES-1, XRES/2, 0, s, c);
# draw_line(XRES-1, 0, 250, YRES-1, s, c);
#
# #horizontal and vertical
# c[BLUE] = 0;
# c[GREEN] = 255;
# draw_line(0, 250, XRES-1, 250, s, c);
# draw_line(250, 0, 250, YRES-1, s, c);
#

seed(2)


for i in range(100):
    c[RED] = 255
    c[BLUE] = randint(0,255)
    c[GREEN] = randint(0,255)

    draw_line(100, 100, 100 + randint(-150, 150), 100 + randint(-150, 150), s, c)


for i in range(100):
    c[RED] = randint(0,255)
    c[BLUE] = 255
    c[GREEN] = randint(0,255)

    draw_line(100, 400, 100 + randint(-150, 150), 400 + randint(-150, 150), s, c)


for i in range(100):
    c[RED] = randint(0,255)
    c[BLUE] = randint(0,255)
    c[GREEN] = 255

    draw_line(400, 100, 400 + randint(-150, 150), 100 + randint(-150, 150), s, c)

for i in range(100):
    c[RED] = 255
    c[BLUE] = randint(0,255)
    c[GREEN] = randint(0,255)

    draw_line(400, 400, 400 + randint(-150, 150), 400 + randint(-150, 150), s, c)


display(s)
save_ppm(s, 'binary.ppm')
save_ppm_ascii(s, 'ascii.ppm')
save_extension(s, 'img.png')
