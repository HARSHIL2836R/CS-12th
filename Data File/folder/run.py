import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
f = open('{}\\folder2\\new.txt'.format(dir_path), 'r')
data= f.read()
print(data)
f.close()