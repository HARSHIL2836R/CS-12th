def my_fun(limit):

    def is_prime(x):
        flag = 1
        for i in range(2, x):
            if x%i == 0:
                flag = 0
        if flag == 0:
            return False
        else:
            return True

    for x in range(1, limit):
        if is_prime(x):
            print(x, end=', ')