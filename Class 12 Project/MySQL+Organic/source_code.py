import mysql.connector
cnx = mysql.connector.connect(host='localhost', port='2836', user='root', passwd='root', database = 'Organic_chem')
cur = cnx.cursor()
_format_ = ['Name', 'Reactant', 'Reagent', 'Conditions', 'Product', 'Remarks']

class helpers():
    def _print_rx_(rx):
        print(*(key+':- '+item for item, key in zip(rx,_format_)), sep='\n')

    def search_term(term, n, rx):
            term1 = input("Enter %s of the reaction you want to search:-   "%term)
            if term1 in rx[n]:
                print("The Reaction is as follows:")
                helpers._print_rx_(rx)
                return rx
            print("The Reaction having such %s could not be found"%term)
            return None

    def change_term(term, term1):
        term2 = input("Enter new %s for the Reaction:- "%term)
        cur.execute("update Reactions set %s='%s' where %s='%s';"%(term, term2, term, term1))
        cnx.commit()
        print("Reaction successfully updated.")
        return True

    def page_break():
        print('-'*120)

class Ops():
    def insert_rx():
        print('<INSERTING A REACTION>')
        v1 = str(input("Enter name:- "))
        v2 = str(input("Enter reactant(s):- "))
        v3 = str(input("Enter reagent(s):- "))
        v4 = str(input("Enter condition(s):- "))
        v5 = str(input("Enter product(s):- "))
        v6 = str(input("Remarks over the reaction (mechanism, explanation, reactivity,...):-   "))
        st = "insert into Reactions values('{}','{}','{}','{}','{}','{}');".format(v1,v2,v3,v4,v5,v6)
        cur.execute(st)
        cnx.commit()
        return True

    def list_db():
        print('<LISTING THE DATABASE>')
        cur.execute('select * from Reactions;')
        data = cur.fetchall()
        i = 1
        for rx in data:
            print('<Reaction %d>'%i)
            helpers._print_rx_(rx)
            helpers.page_break()
            i+=1
        if data == []:
            print("Database is Empty.")
        return

    def search_db():
        print('<SEARCHING THE DATABASE>')
        print('''By which parameter would you like to search for reaction?
    1. Name
    2. Reactant
    3. Reagent
    4. Conditions
    5. Product
    (6. Remarks (searches same as 7.))
    7. Search in all
        ''')
        cur.execute('select * from Reactions;')
        data = cur.fetchall()
        i = input("Enter your choice (1-6):-  ")
        helpers.page_break()
        for rx in data:
            if int(i) == 1:
                return helpers.search_term('Name',0,rx)
            if int(i) == 2:
                return helpers.search_term('Reactant',1,rx)
            if int(i) == 3:
                return helpers.search_term('Reagent',2,rx)
            if int(i) == 4:
                return helpers.search_term('Conditions',3,rx)
            if int(i) == 5:
                return helpers.search_term('Product',4,rx)
            if int(i) == 6 or 7:
                a = input("Enter the term present in the reaction:-   ")
                for rx in data:
                    for el in rx:
                        if a in el:
                            print("The Reaction is as follows:")
                            helpers._print_rx_(rx)
                            return rx
                print("None of the Reactions contain this term")
                return None
            else:
                print("There was an error in the input, execute again")
                return None

    def update_db():
        print('<UPDATING A REACTION')
        print("First search for the reaction you want to update: ")
        try:
            rx = Ops.search_db()
            rx = list(rx)
            i = int(input("Enter the term you want to update(1-6):- "))
            if i == 1:
                helpers.change_term('Name', rx[0])
            if i == 2:
                helpers.change_term('Reactant', rx[1])
            if i == 3:
                helpers.change_term('Reagent', rx[2])
            if i == 4:
                helpers.change_term('Conditions', rx[3])
            if i == 5:
                helpers.change_term('Product', rx[4])
            if i == 6:
                helpers.change_term('Remarks', rx[5])
            return
        except ValueError or TypeError:
            return

    def delete_rx():
        print('<DELETING A REACTION>')
        print("First search for the reaction you want to delete: ")
        try:
            rx = Ops.search_db()
            cur.execute("delete from Reactions where {}='{}';".format('Name', rx[0]))
            cnx.commit()
            helpers.page_break()
            print("Reaction successfully deleted.")
        except ValueError or TypeError:
            return

class Interface():
    def operations():
        helpers.page_break()
        print('''
    Operations:- 

    1. Add Reaction to database
    2. List out the database
    3. Search the database
    4. Update reaction(s)
    5. Delete a reaction

    Select the operation you want to perform (1-4):    ''', end='')

        try:
            i = int(input())
            helpers.page_break()
            if i == 1:
                return Ops.insert_rx()
            elif i == 2:
                return Ops.list_db()
            elif i == 3:
                return Ops.search_db()
            elif i == 4:
                return Ops.update_db()
            elif i == 5:
                return Ops.delete_rx()

        except TypeError:
            print("There was error in the input. Execute again.")
            return

    def _init_():
        print('''
                        ----------------------------------------------------------------
                        ###############################################################
                        |>---<|This is a database of Organic Chemistry Reactions|>---<|
                        ###############################################################
                        ----------------------------------------------------------------
    ''')
        while True:
            Interface.operations()


Interface._init_()