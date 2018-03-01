from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [ 255, 0, 0 ]
edges = []
transform = new_matrix()

#dw test file
parse_file( 'script', edges, transform, screen, color )

'''
#henry test file
parse_file( 'tbw', edges, transform, screen, color )
'''
