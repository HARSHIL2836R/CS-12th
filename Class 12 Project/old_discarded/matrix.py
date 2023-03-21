class Basics():

    def _make_matrix_by_gf_(a, m, n):
        ''' a(i, j) is a function of 
        i (representing row number) and j (representing column number) 
        and it represents the general term of matrix '''
        
        A = [[a(x, y) for y in range(1,n+1)] for x in range(1, m+1)]

        return A

    def _make_matrix_manually_(m,n):
        M = []
        for i in range(m):
            try:
                r = input("Enter %sth row of matrix (Elements separated by commas): "%(i+1))
            except len(r.split(','))!=3:
                print("Wrong row entered for specified matrix, Try Again.")
                return
            M.append([int(x) for x in r.split(',') if x.isdigit()])
        print(M)
        return M

class Algebraic_Properties():
    def Addition(*A):
        _sum_ = [[]*len(A)]
        return _sum_