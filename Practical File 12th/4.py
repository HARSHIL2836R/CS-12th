# Write a program to generate random numbers between 1 to 6 and check whether a user won a lottery or not

import random
def __main__():

    r_num = random.randint(1,6)
    if int(input('Enter any integer between 1 and 6(both included):- ')) == r_num:
        print("You won a lottery! Your number matched the randomly generated number.")
    else:
        print("You didn't win lottery. Your number did not matched the randomly generated number (%d)."%(r_num))
    
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