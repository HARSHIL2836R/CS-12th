import mysql.connector
cnx = mysql.connector.connect(host='localhost', port='2836', user='root', passwd='root', database = 'demo')
cur = cnx.cursor()
cur.execute('select* from demo_t;')
data= cur.fetchall()
print(data)