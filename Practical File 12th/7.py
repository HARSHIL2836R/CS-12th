# Write a function FACT( ) to calculate the factorial of an integer.

def __main__():
    def FACT(n):
        return 1 if (n == 1 or n == 0) else n*FACT(n-1)
    n = int(input("Enter Number:- "))
    print("Factorial of the given number is ", FACT(n))

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