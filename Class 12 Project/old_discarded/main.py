import matrix
import math

def print_matrix(M):
    for el in M:
        print(el)


def make_matrix():
    A = input("Enter expression for element aij :")
    def a(i,j):
        """Enter the expression for the general term of matrix
        (It should be in form of numerals with i and j as variables representing 
        row number and column number respectively)"""
        return eval(A)

    m = int(input("Enter number of rows in matrix:- ")) 
    n = int(input("Enter number of columns in matrix:- "))
    print("The Matrix is:-")
    M = matrix.Basics._make_matrix_by_gf(a, m, n)
    print_matrix(M)

def __init__():
    print('''
1. Make matrix
2. Exit
    ''')
    i = int(input('Enter your choice:-'))
    if i == 1:
        make_matrix()
    elif i == 2:
        exit()

__init__()