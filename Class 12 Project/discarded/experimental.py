def a(i,j):
    ''' Expression for the general term '''
    return (0.5)*abs((-3)*i + j)

def _make_matrix_(a, m, n):
        # let a(i,j) be a function of i and j 
        # and represent the general term of matrix
        
        A = [[a(x, y) for y in range(1,n+1)] for x in range(1, m+1)]
        
        for el in A:
            print(el)

_make_matrix_(a, 3, 4)