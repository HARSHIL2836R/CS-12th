# Write a program to display ASCII code of a character and vice versa.

def __main__():
    # checking what to do
    check = int(input('Do you want to convert ASCII to character or character to ASCII?(1 for first and 2 for second choice):- '))

    if check == 2:
        # character to ascii
        char = input("Enter the character:- ")
        print("ASCII value of " + str(char) + " is " + str(ord(char)))

    elif check == 1:
        # ascii to character
        asc = int(input("Enter the ASCII value:- "))
        print("The character with ASCII value " + str(asc)+ " is " + str(chr(asc)))

    else:
        print("You have to type 1 or 2 only.")

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