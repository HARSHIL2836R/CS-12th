import matrix

def a(i, j):
    """Enter the expression for the general term of matrix
    (It should be in form of numerals with i and j as variables representing 
    row number and column number respectively)"""
    return 2*i + 2*j**2

m = int(input("Enter number of rows in matrix:- ")) 
n = int(input("Enter number of columns in matrix:- "))

print("The Matrix is:-")

for el in matrix.Basics._make_matrix_(a, m, n):
    print(el)