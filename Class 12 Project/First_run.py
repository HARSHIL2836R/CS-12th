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
    cur.execute("insert into Reactions values(%s)"%(v1,v2,v3,v4,v5))

def list_db():
    data = cur.execute('select * from Reactions;')
    for rx in data:
        #CHECK
        print(*(key+':-    '+item for item in rx for key in _format_), sep='\n')
        print('\n')

def _init_():
    print('''
-------------------------------------------------------------------
  ###############################################################
  |>---<|This is a database of Organic Chemistry Reactions|>---<|
  ###############################################################
-------------------------------------------------------------------
''')
    print('''
Operations:- 

1. Add Reaction to database
2. List out the database
3. Search the database

Select the operation you want to perform (1-3):    ''')
    i = int(input())
    if i == 1:
        insert_rx()
    if i == 2:
        list_db()
    if i == 3:
        search_db()