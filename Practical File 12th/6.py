# Write a program to compute GCD and LCM of two numbers using functions.

def __main__():
    def GCD(a,b):
        val = 0
        for i in range(max(a,b), 0, -1):
            if a % i == 0 and b % i == 0:
                val = i
                break
        return val

    def LCM(a,b):
        val = 0
        j = 1
        while j != 0:
            if j % a == 0 and j % b == 0:
                val = j
                j = -1
            j += 1
        return val

    x,y = int(input("Enter two numbers:-\nNumber 1:- ")), int(input("Number 2:- "))
    print("GCD of numbers is:- ", GCD(x,y))
    print("LCM of numbers is:- ", LCM(x,y))

def __code_continue__(func):
    global __flag__
    func() # Main code run
    __flag__ = 1
    while __flag__ == 1:
        if int(input('\nDo you want to continue?(1 for yes, 0 for no):-')) == 1:
            print("New Instance-> \n------------------------------------------------------------------")
            __code_continue__(func)
        else:
            __flag__ = 0

__code_continue__(__main__)