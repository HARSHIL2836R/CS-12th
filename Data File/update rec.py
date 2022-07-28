import pickle
stu = {}
found = False
fin = open('stu.dat', 'rb+')
try:
    while True:
        rpos = fin.tell()
        stu = pickle.load(fin)
        if stu['Marks'] > 81:
            stu['Marks'] += 2
            fin.seek(rpos)
            pickle.dump(stu, fin)
            found = True
except EOFError:
    if found == False:
        print("Sorry, no matching record found.")
    else:
        print("Record(s) successfully updated.")
    fin.close()