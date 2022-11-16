f = open('a.txt','r')
new_l = []
for line in f.readlines():
    if line[0] == 'p':
        new_l.append(line)
f.close()
h = open('newfile.txt', 'w')
for line in new_l:
    h.write(line)
h.close()