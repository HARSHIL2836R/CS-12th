# Write a function SwapNumbers( ) to swap two numbers 
# and display the numbers before swapping and after swapping

def __main__():
    def SwapNumbers(a,b):
        print("Before swapping:- %s, %s"%(a,b))
        a,b = b,a
        print("After swapping:- %s, %s"%(a,b))
    SwapNumbers(1,2)

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