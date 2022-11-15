#Write a menu based program to perform the operation on stack in python.

def isEmpty(stk):
    if stk == []:
        return True
    else:
        return False

def Push(stk, itm):
    stk.append(itm)
    return

def Pop(stk):
    return stk.pop()

def Peek(stk):
    return stk[-1]

def Display(stk):
    print("Stack is:- \n")
    for el in stk:
        print(el)
    return

#Main
stack = []
while True:
    print('''
--------------------------------------------------------------

STACK OPERATIONS
1. Push
2. Pop
3. Peek
4. Display Stack
5. Exit

    ''')
    ch = int(input('Enter your choice (1-5):- '))
    if ch == 1:
        Push(stack, input('Enter item to be pushed:- '))
    if ch == 2:
        if isEmpty(stack):
            print("Underflow! Stack is Empty!")
        else:
            r = Pop(stack)
            print("Popped item is:- ", r)
    if ch == 3:
        if isEmpty(stack):
            print("Underflow! Stack is Empty!")
        else:
            t = Peek(stack)
            print("Topmost item is:- ", t)
    if ch == 4:
        if isEmpty(stack):
            print("Stack is empty")
        else:
            Display(stack)
    if ch == 5:
        break