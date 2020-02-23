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
    for x in range (len (m2)): #columns in m2
        ans = [] #sums per column
        for y in range (len (m2[0])): #rows
            sum = 0
            for z in range (len (m1)):
                sum += (m1[z][y] * m2[x][z])
            ans.append (sum)
        m2[x] = ans

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

a = [[21,31,41,51],
     [2,4,7,1],
     [20, 10, 0, 2],
     [1,1,1,1]]

b = [[2,4,7,1],
     [20, 10, 0, 2],
     [21,31,41,51],
     [1,1,1,1]]

print ("Matrix A RN:\n")
print_matrix (a)
print ("\n")

print ("Matrix B RN: \n")
print_matrix (b)
print ("\n")

print ("Row 2 of A: ")
print (return_row (a,2))
print ("Col 1 of A: ")
print (return_col (a,1))

print ("\n")
print ("Row 2 of B: ")
print (return_row (b,2))
print ("Col 2 of B: ")
print (return_col (b,2))


print ("multiplying A and B, B becomes the product\n")
matrix_mult (a,b)
print_matrix (b)
