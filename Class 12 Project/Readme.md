## MATRICES IN PYTHON

# Matrix in python:

example, the matrix

| 12 14 13 |
| 11 12 10 |
| 13 11 12 |

can be represented as:

[[12, 14, 13], [11, 12, 10], [13, 11, 12]]

# Generalisation:

A matrix of order m x n with general term expression a(i, j) can be represented as :
A = [[a(x, y) for y in range(1,n+1)] for x in range(1, m+1)]

len(A) represents number of rows
len(A[0]) represents number of columns