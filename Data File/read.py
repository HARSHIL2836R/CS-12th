import pickle
f = open('stu.dat','rb')
try:
    while True:
        d = pickle.load(f)
        print(d)
except EOFError:
    f.close()