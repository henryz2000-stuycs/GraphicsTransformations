import math

def make_translate( x, y, z ):
    '''
    m1 = [ [1, 0, 0, x], \
           [0, 1, 0, y], \
           [0, 0, 1, z], \
           [0, 0, 0, 1] ]
    '''
    m1 = new_matrix(4, 4)
    ident(m1)
    m1[3][0] = x
    m1[3][1] = y
    m1[3][2] = z
    #print_matrix(m1)
    return m1

def make_scale( x, y, z ):
    '''
    m1 = [ [x, 0, 0, 0], \
           [0, y, 0, 0], \
           [0, 0, z, 0], \
           [0, 0, 0, 1] ]
    '''
    m1 = new_matrix(4, 4)
    ident(m1)
    m1[0][0] = x
    m1[1][1] = y
    m1[2][2] = z
    return m1

def make_rotX( theta ):
    '''
    m1 = [ [1,                               0,                                    0, 0], \
           [0, math.cos(theta * math.pi / 180), -1 * math.sin(theta * math.pi / 180), 0], \
           [0, math.sin(theta * math.pi / 180),      math.cos(theta * math.pi / 180), 1], \
           [0,                               0,                                    0, 1] ]
    '''
    m1 = new_matrix(4, 4)
    ident(m1)
    m1[1][1] = math.cos(theta * math.pi / 180)
    m1[2][1] = -1 * math.sin(theta * math.pi / 180)
    m1[1][2] = math.sin(theta * math.pi / 180)
    m1[2][2] = math.cos(theta * math.pi / 180)
    return m1

def make_rotY( theta ):
    '''
    m1 = [ [     math.cos(theta * math.pi / 180), 0, math.sin(theta * math.pi / 180), 0], \
           [                                   0, 1,                               0, 0], \
           [                                   0, 0,                               1, 0], \
           [-1 * math.sin(theta * math.pi / 180), 0, math.cos(theta * math.pi / 180), 1] ]
    '''
    m1 = new_matrix(4, 4)
    ident(m1)
    m1[0][0] = math.cos(theta * math.pi / 180)
    m1[2][0] = math.sin(theta * math.pi / 180)
    m1[0][3] = -1 * math.sin(theta * math.pi / 180)
    m1[2][3] = math.cos(theta * math.pi / 180)
    return m1

def make_rotZ( theta ):
    '''
    m1 = [ [math.cos(theta * math.pi / 180), -1 * math.sin(theta * math.pi / 180), 0, 0], \
           [math.sin(theta * math.pi / 180),      math.cos(theta * math.pi / 180), 0, 0], \
           [                              0,                                    0, 1, 0], \
           [                              0,                                    0, 0, 1] ]
    '''
    m1 = new_matrix(4, 4)
    ident(m1)
    m1[0][0] = math.cos(theta * math.pi / 180)
    m1[1][0] = -1 * math.sin(theta * math.pi / 180)
    m1[0][1] = math.sin(theta * math.pi / 180)
    m1[1][1] = math.cos(theta * math.pi / 180)
    return m1

def print_matrix( matrix ):
    s = ''
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            s+= str(matrix[c][r]) + ' '
        s+= '\n'
    print s

def ident( matrix ):
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            if r == c:
                matrix[c][r] = 1
            else:
                matrix[c][r] = 0

def scalar_mult( matrix, s ):
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            matrix[c][r]*= s
            
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):

    point = 0
    for row in m2:
        #get a copy of the next point
        tmp = row[:]
        
        for r in range(4):
            m2[point][r] = (m1[0][r] * tmp[0] +
                            m1[1][r] * tmp[1] +
                            m1[2][r] * tmp[2] +
                            m1[3][r] * tmp[3])
        point+= 1


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

'''
m1 = new_matrix(4, 4)
ident(m1)
make_translate(100, 100, 0)
'''
