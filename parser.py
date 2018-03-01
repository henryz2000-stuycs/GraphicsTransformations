from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
     line: add a line to the edge matrix - 
	    takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
	 ident: set the transform matrix to the identity matrix - 
	 scale: create a scale matrix, 
	    then multiply the transform matrix by the scale matrix - 
	    takes 3 arguments (sx, sy, sz)
	 move: create a translation matrix, 
	    then multiply the transform matrix by the translation matrix - 
	    takes 3 arguments (tx, ty, tz)
	 rotate: create a rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 2 arguments (axis, theta) axis should be x, y or z
	 apply: apply the current transformation matrix to the 
	    edge matrix
	 display: draw the lines of the edge matrix to the screen
	    display the screen
	 save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    points = new_matrix(4, 4)
    f = open(fname, 'r')
    lines = f.readlines()
    #print lines
    #print len(lines)
    for i in range(len(lines)):
        #print i
        if lines[i] == "line\n":
            print "==line=="
            coords = lines[i+1].split(" ")
            add_edge(points, int(coords[0]), int(coords[1]), int(coords[2]), int(coords[3]), int(coords[4]), int(coords[5]))
        elif lines[i] == "ident\n":
            print "==ident=="
            ident(transform)
            print "transform matrix"
            print_matrix(transform)
        elif lines[i] == "scale\n":
            print "***scale***"
            coords = lines[i+1].split(" ")
            scale = make_scale(float(coords[0]), float(coords[1]), float(coords[2]))
            print "scale matrix"
            print_matrix(scale)
            matrix_mult(scale, transform)
            print "transform matrix"
            print_matrix(transform)
        elif lines[i] == "move\n":
            print "***move***"
            coords = lines[i+1].split(" ")
            translate = make_translate(int(coords[0]), int(coords[1]), int(coords[2]))
            print "translate matrix"
            print_matrix(translate)
            print "transform matrix"
            matrix_mult(translate, transform)
        elif lines[i] == "rotate\n":
            print "***rotate***"
            coords = lines[i+1].split(" ")
            if coords[0] == "x":
                rotate = make_rotX(int(coords[1]))
            elif coords[0] == "y":
                rotate = make_rotY(int(coords[1]))
            else:
                rotate = make_rotZ(int(coords[1]))
            print "rotate matrix"
            print_matrix(rotate)
            print "transform matrix"
            matrix_mult(rotate, transform)
        elif lines[i] == "apply\n":
            print "==apply=="
            print "transform matrix"
            print_matrix(transform)
            print "edge matrix"
            print_matrix(points)
            matrix_mult(transform, points)
        elif lines[i] == "display\n":
            print "==display=="
            clear_screen(screen)
            #print_matrix(points)
            for row in range(len(points)):
                for col in range(len(points[row])):
                    points[row][col] = int(points[row][col])
            print_matrix(points)
            draw_lines(points, screen, color)
            display(screen)
        elif lines[i] == "save\n":
            print "==save=="
            imgname = lines[i+1]
            save_extension(screen, imgname)
        else:
            pass
        
