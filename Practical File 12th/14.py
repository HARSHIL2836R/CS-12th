import pickle
f = open('a.dat', 'ab')
n = int(input('Number of entries to add:-'))
if n != 0:
    for _ in range(n):
        rec = []
        rec.append(input("Enter name:- "))
        rec.append(int(input("Enter Roll number:- ")))
    pickle.dump(rec, f)
f.close()

print("\nReading Data\n")
h = open('a.dat','rb')
try:
    while True:
        data = pickle.load(h)
        print("Name: ", data[0])
        print("Roll No.: %d\n"%data[1])
        
except EOFError:
    h.close()