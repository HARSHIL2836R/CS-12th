f = open('Data File\\a.txt', 'r')
print(''.join(reversed(f.read())))
f.close()