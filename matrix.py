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
    ans =[]
    for i in range (len (m1)):
        r = []
        for j in range (len (m2[0])):
            col = return_col (m1, i)
            row = return_row (m2,j)
            sum = mult_row_col (col,row)
            r.append (sum)
        ans.append (r)
    m2 = ans
    return m2


    # ans_r, ans_c = 0,0
    # for col in range (len(m1)):
    #     sum = 0
    #     for row in range (len (m1[col])):
    #         sum += (m1[col][row]*m2[row][col])
    #     ans[ans_r][ans_c] = sum
    #     ans_r += 1
    #     ans_c += 1

def return_row (matrix, index):
    return matrix[index]

def return_col (matrix, index):
    ans = []
    for i in range (len (matrix)):
        ans.append (matrix[i][index])
    return ans

def mult_row_col (col, row):
    sum = 0
    for i in range (len (col)):
        sum += (col[i] * row[i])
    return sum

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

b = new_matrix ()
b[0] = [2,4,7,1]
b[1] = [20, 10, 0, 2]
b[2] = [21,31,41,51]
b[3] = [1,1,1,1]

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
