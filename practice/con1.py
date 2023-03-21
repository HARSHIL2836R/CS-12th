import mysql.connector as ctor
dbcon = ctor.connect(host = 'localhost', user='root', passwd='root', database='demo', port='2836')
cursor = dbcon.cursor()
sql1="delete from the_view where name = '%s'"
data1 = ('Nishant',)
cursor.execute(sql1%data1)
dbcon.commit()
print("Rows affected: ", cursor.rowcount)
dbcon.close()