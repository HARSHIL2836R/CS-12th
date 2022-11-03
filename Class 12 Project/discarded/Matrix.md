# MATRICES IN PYTHON

## Matrix in python:

example, the matrix

| 12 14 13 |<br>
| 11 12 10 |<br>
| 13 11 12 |<br>

can be represented as:

[[12, 14, 13], [11, 12, 10], [13, 11, 12]]

## Generalisation:

A matrix of order m x n with general term expression a(i, j) can be represented as :<br>

A = [[a(x, y) for y in range(1,n+1)] for x in range(1, m+1)]

len(A) represents number of rows<br>
len(A[0]) represents number of columns<br>
