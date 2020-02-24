from display import *
from draw import *
from matrix import *
import random

screen = new_screen()
GREY = [ 169, 169, 169 ]
matrix = new_matrix()

# TESTING DRAWING A SQUARE
# add_edge (matrix, 50,50, 0, 150, 50,0)
# add_edge (matrix, 150, 50,0, 150, 150, 0)
# add_edge (matrix, 150, 150, 0, 50, 150, 0)
# add_edge (matrix, 50,50, 0, 50, 150, 0)

def draw_road ():
    add_edge (matrix, 0, 250, 0, 500, 250, 0)

draw_road ()

def draw_legs ():
    x = 75
    while (x < 500):
        add_edge (matrix, x, 250, 0, x, 0, 0)
        add_edge (matrix, x, 0, 0, x + 40, 0, 0)
        add_edge (matrix, x + 40, 0, 0, x + 40, 250, 0)
        x += 300

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

draw_lines( matrix, screen, GREY )
display(screen)
