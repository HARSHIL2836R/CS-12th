import pickle
from unicodedata import name
stu = {}
stufile = open('stu.dat','wb')
ans = 'y'
while ans == 'y':
    rno = int(input('Enter roll number:-'))
    name = input("Enter name:- ")
    marks = float(input('Enter marks:- '))
    stu['Rollno']= rno
    stu['Name']=name
    stu['Marks']= marks
    pickle.dump(stu,stufile)
    ans = input("Want to enter more records?(y/n)... ")
stufile.close()