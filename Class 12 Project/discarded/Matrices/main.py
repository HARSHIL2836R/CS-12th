import mysql.connector
mycon = mysql.connector.connect(host='localhost', user='root', passwd='root', database='matrices')
cursor=mycon.cursor()
class Types():
    def main():
        r1 = Types.show_types()
        if r1 == exit:
            pass

        
    def show_types():
        cursor.execute('select serial_no, name from types;')
        data=cursor.fetchall()
        for row in data:
            print(row[0]," : ", row[1])
        return input("Enter code to know more:- ")
