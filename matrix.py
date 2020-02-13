"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    row1, row2, row3,row4 = "","", "", ""
    for i in range (len (matrix)):
        row1 += str (matrix[i][0]) + " "
        row2 += str (matrix[i][1]) + " "
        row3 += str (matrix[i][2]) + " "
        row4 += str (matrix[i][3]) + " "
    print (row1)
    print (row2)
    print (row3)
    print (row4)

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    for i in range (len(matrix)):
        for j in range (len (matrix[i])):
            if i == j:
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    ans = new_matrix
    for i in range (len(m1)):
        sum = 0
        for j in range (len (m2[i])):
            sum += m1[i]
    m2 = ans

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

a = new_matrix ()
a[0] = [21,31,41,51]
a[1] = [2,4,7,1]
a[2] = [20, 10, 0, 2]
a[3] = [1,1,1,1]

print ("Matrix RN:\n")
print_matrix (a)
print ("\n")

print ("Now It's an Identity Matrix:\n")
ident (a)
print_matrix (a)
print ("\n")
