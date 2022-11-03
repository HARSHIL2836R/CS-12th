class Basics():

    def _make_matrix_(a, m, n):
        ''' a(i, j) is a function of 
        i (representing row number) and j (representing column number) 
        and it represents the general term of matrix '''
        
        A = [[a(x, y) for y in range(1,n+1)] for x in range(1, m+1)]

        return A

class Algebraic_Properties():
    def Addition(*A):
        _sum_ = [[]*len(A)]
        return _sum_