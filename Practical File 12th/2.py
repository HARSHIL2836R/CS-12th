# Write a program to check a number whether it is palindrome or not.

def __main__():
    num = str(input("Enter the number:- "))
    palindrome = True
    for i in range(0, int(len(num)/2)):
        if num[i] != num[len(num)-i-1]:
            palindrome = False
    if palindrome:
        print("The number is a palindrome.")
    else:
        print("The number is not a palindrome.")

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