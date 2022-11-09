import mysql.connector
cnx = mysql.connector.connect(host='localhost', user='root', passwd='root')
cur = cnx.cursor()
_format_ = ['Name', 'Reactant', 'Reagent', 'Conditions', 'Product', 'Remarks']

def insert_rx():
    v1 = str(input("Enter reactant(s):- "))
    v2 = str(input("Enter reagent(s):- "))
    v3 = str(input("Enter condition(s):- "))
    v4 = str(input("Enter product(s):- "))
    v5 = str(input("Remark over the reaction (mechanism, explanation, reactivity,...):-   "))
    cur.execute("insert into Reactions values(%s);"%(v1,v2,v3,v4,v5))

def _print_rx_(rx):
    print(*(key+':-    '+item for item, key in zip(rx,_format_)), sep='\n')

def list_db():
    data = cur.execute('select * from Reactions;')
    for rx in data:
        _print_rx_(rx)
        print('\n')
    return

def search_db():
    data = cur.execute('select * from Reactions;')
    print('''By which parameter would you like to search for reaction?
1. Name
2. Reactant
3. Reagent
4. Conditions
5. Product
6. In all of it

    ''')
    i = input("Enter number(1-6):-  ")
    if int(i) == 1:
        name = input("Enter Name of the reaction you want to search:-   ")
        for rx in data:
            if name in rx(0):
                print("The Reaction is as follows:")
                _print_rx_(rx)
                return rx
    if int(i) == 2:
        react = input("Enter Reactant(s) of the reaction you want to search:-   ")
        for rx in data:
            if react in rx(1):
                print("The Reaction is as follows:")
                _print_rx_(rx)
                return rx
        print("The Reaction could not be found")
        return
    if int(i) == 3:
        reag = input("Enter Reagent(s) of the reaction you want to search:-   ")
        for rx in data:
            if reag in rx(2):
                print("The Reaction is as follows:")
                _print_rx_(rx)
                return rx
        print("The Reaction could not be found")
        return
    if int(i) == 4:
        con = input("Enter the conditions of the reaction you want to search:-   ")
        for rx in data:
            if con in rx(3):
                print("The Reaction is as follows:")
                _print_rx_(rx)
                return rx
        print("The Reaction could not be found")
        return
    if int(i) == 5:
        pro = input("Enter the Product(s) of the reaction you want to search:-   ")
        for rx in data:
            if pro in rx(4):
                print("The Reaction is as follows:")
                _print_rx_(rx)
                return rx
        print("The Reaction could not be found")
        return
    if int(i) == 6:
        a = input("Enter the term present in the reaction:-   ")
        for rx in data:
            for el in rx:
                if a in el:
                    print("The Reaction is as follows:")
                    _print_rx_(rx)
                    return rx
        print("The Reaction could not be found")
        return
    else:
        print("There was an error in the input, execute again")
        
    operations()

def update_db():
    print("First search for the reaction you want to update: ")
    try:
        rx = search_db()
        rx = list(rx)
        i = int(input("Enter the term you want to update(1-5):- "))
        #CONTINUE FROM HERE

    except ValueError or TypeError:
        print("There is some error in the inout. Execute again.")
        return
def operations():

    print('''
Operations:- 

1. Add Reaction to database
2. List out the database
3. Search the database
4. Update reaction(s)

Select the operation you want to perform (1-4):    ''')

    try:
        i = int(input())
        if i == 1:
            insert_rx()
        if i == 2:
            list_db()
        if i == 3:
            search_db()
        if i == 4:
            update_db()
    except TypeError:
        print("There was error in the input. Execute again.")
        operations()

def _init_():
    print('''
-------------------------------------------------------------------
  ###############################################################
  |>---<|This is a database of Organic Chemistry Reactions|>---<|
  ###############################################################
-------------------------------------------------------------------
''')
    operations()


_init_()