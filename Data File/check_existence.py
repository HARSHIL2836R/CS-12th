try:
    f=open('Data File\\a.txt','r')
    print("File exists.")
    f.close()
except:
    print("File does not exist.")