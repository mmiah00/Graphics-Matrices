from display import *
from draw import *
from matrix import *
import random

screen = new_screen()
WHITE = [ 255, 255, 255 ]
matrix = new_matrix()

# TESTING DRAWING A SQUARE
# add_edge (matrix, 50,50, 0, 150, 50,0)
# add_edge (matrix, 150, 50,0, 150, 150, 0)
# add_edge (matrix, 150, 150, 0, 50, 150, 0)
# add_edge (matrix, 50,50, 0, 50, 150, 0)

# add_edge (matrix, 0, 350, 0, 0, 360, 0)
def draw_road ():
    add_edge (matrix, 0, 250, 0, 500, 250, 0)
    #add_edge (matrix, 0, 260, 0, 500, 260, 0)
    # add_edge (matrix, 500, 300, 0, 500, 150, 0)
    # add_edge (matrix, 500, 300, 0, 0, 360, 0)
    # add_edge (matrix, 500, 150, 0, 0, 350, 0)

draw_road ()

def draw_legs ():
    x = 75
    while (x < 500):
        add_edge (matrix, x, 250, 0, x, 0, 0)
        add_edge (matrix, x, 0, 0, x + 40, 0, 0)
        add_edge (matrix, x + 40, 0, 0, x + 40, 250, 0)
        x += 300
        # y1 = int ((-2/5)*x + 350)
        # add_edge (matrix, x, y1, 0, x, y1 - 75, 0)
        # add_edge (matrix, x, y1 - 75, 0, x + 25, y1 - 75, 0)
        # y2 = int ((-2/5)*(x + 25) + 350)
        # add_edge (matrix, x + 25, y1 - 75, 0, x + 25, y2, 0)
        # x += 75

draw_legs ()

def draw_cables (starting_x, ending_x):
    y = 250 + 175 - 25
    while (y > 250):
        add_edge (matrix, starting_x, y, 0 , ending_x, 250, 0)
        y -= 20

def draw_beams ():
    x = 85
    draw_cables (x, x - 145)
    while (x < 500):
        add_edge (matrix, x, 250, 0, x, 250 + 175, 0)
        add_edge (matrix, x, 250 + 175, 0, x + 20, 250 + 175, 0)
        add_edge (matrix, x + 20, 250 + 175, 0, x + 20, 250, 0)
        draw_cables (x + 20, x + 160)
        draw_cables (x + 300, x + 160)
        x += 300

draw_beams ()



draw_lines( matrix, screen, WHITE )
display(screen)
