f = open('d:\\Documents\\Class 12th\\CS-12\\Data File\\a.txt','r')
data = f.read()
count = 0
for el in data.split():
    try:
        if int(el.strip(',.')):
            count+=1
    except:
        continue
print(count)
f.close()