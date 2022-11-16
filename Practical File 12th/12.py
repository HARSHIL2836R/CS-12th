f = open("a.txt",'r')
data = f.read()
count = 0
for el in data.split():
    if el.strip(',.') == 'is':
        count+=1
print("Occurence of 'is' is %d times"%count)
f.close()