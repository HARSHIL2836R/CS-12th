import mysql.connector
cnx = mysql.connector.connect(host='localhost', port='2836', user='root', passwd='root', database = 'demo')
cur = cnx.cursor()
st = "insert into demo_t values(%s,%s,%s)"%('me','you','us')
cur.execute(st)