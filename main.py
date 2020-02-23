from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

add_edge (matrix, 50,50, 0, 150, 50,0)
add_edge (matrix, 150, 50,0, 150, 150, 0)
add_edge (matrix, 150, 150, 0, 50, 150, 0)
add_edge (matrix, 50,50, 0, 50, 150, 0)

draw_lines( matrix, screen, color )
display(screen)
