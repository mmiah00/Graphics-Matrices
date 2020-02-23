from display import *
from draw import *
from matrix import *
import random

screen = new_screen()
GREEN = [ 20, 82,80 ]
matrix = new_matrix()

# TESTING DRAWING A SQUARE
# add_edge (matrix, 50,50, 0, 150, 50,0)
# add_edge (matrix, 150, 50,0, 150, 150, 0)
# add_edge (matrix, 150, 150, 0, 50, 150, 0)
# add_edge (matrix, 50,50, 0, 50, 150, 0)

def leaf (radius, cx1, cy1, cx2, cy2):
    for x in range (500):
        for y in range (500):
            if pow ((x - cx1),2) + pow ((y - cy1),2) < pow (radius, 2):
                if pow ((x - cx2),2) + pow ((y - cx2),2) < pow (radius, 2):
                    add_point (matrix, x, y)

leaf (100, 250 - 25, 250, 250 +50, 250)
# DRAWING STAR
# add_edge (matrix, 50, 100, 0, int((50+75)/2), 130,0)
# add_edge (matrix, int((50+75)/2), 130,0, 75, 100, 0)
# add_edge (matrix, 75, 100, 0, 75+32, 100, 0)
# add_edge (matrix, 75+32, 100, 0, 75+15, 100-20,0)
# add_edge (matrix, 50, 100, 0, 50-32, 100, 0)
# add_edge (matrix, 50-32, 100, 0, 50-15, 100-20, 0)
# add_edge (matrix, 75+15, 100-20,0, 75+32, 100-50, 0)
# add_edge (matrix, 75+32, 100-50, 0, 75+15-20, 100-20-15,0)

draw_lines( matrix, screen, GREEN )
display(screen)
