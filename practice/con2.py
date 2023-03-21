import mysql.connector as ctor
mycon = ctor.connect(host='localhost', user='root', passwd='root',port=2836, database='demo')
mycursor = mycon.cursor()
mycursor.execute('select * from student where marks > 350;')
print(mycursor.column_names)
data = mycursor.fetchall()
for row in data:
    print(row)