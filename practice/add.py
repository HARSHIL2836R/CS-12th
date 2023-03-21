import csv
tid = input("Enter teacher ID: ")
tname = input("Enter teacher name: ")
mobile = int(input('Enter mobile number:'))

with open('me.csv','a') as f:
    writer = csv.writer(f)
    row = [tid, tname, mobile]
    writer.writerow(row)
    