import mysql.connector
demodb = mysql.connector.connect(host='localhost', port='2836', user='root', passwd='root', database='demo')
democursor = demodb.cursor(buffered=True)

democursor.execute('select * from student;')
print(democursor.fetchone())

democursor.execute('select * from student;')
print(democursor.fetchall())

democursor.execute('select * from student;')
print(democursor.fetchmany(3))
democursor.execute('select * from student;')

input()