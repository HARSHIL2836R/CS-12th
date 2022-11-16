#Write a program to Create a CSV file by entering user-id and password, read and search the password for given user-id.
import csv

with open('19.csv','a') as f:
    w = csv.writer(f)
    n=int(input("How many userid you want to enter: "))
    for i in range(1,n+1):
        id = input("Enter user-id %d:- "%(i))
        passw = input("Enter Password:- ")
        w.writerow([id,passw])

userid=input("Enter userid for which you want to search password:- ")
with open('19.csv','rt') as f:
    flag = 0
    data = csv.reader(f)
    for row in data:
        if row != [] and row[0] == userid:
            print('Password is:- ', row[1])
            flag = 1
            break
    if flag == 0:
        print('User not found')