# Write a program in python to check a number whether it is prime or not

def __main__():
    num = int(input("Enter the number:- "))
    prime = True #Assigning a variable
    for i in range(2, int(num**(1/2))+1):
        if num%i == 0:
            prime = False
            break
    if prime:
        print("The number is a prime number.")
    else:
        print("The number is not a prime number.")

def __init__():
    global conf
    conf = int(input("Do you want to continue?(1 for yes, 0 for no):- "))
    while conf == 1:
        __main__() #First inititalisation
        __init__()

__main__() #First initiation
__init__()