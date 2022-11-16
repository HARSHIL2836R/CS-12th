#Write a program to pass an integer list as stack to a function and push only those elements in the stack which are divisible by 7.
stack = []
def push_7s(int_list):
    for el in int_list:
        if int(el) % 7 == 0:
            stack.append(el)
push_7s([0,1,2,7,14,99,95,49])
print("The stack is:- ", stack)