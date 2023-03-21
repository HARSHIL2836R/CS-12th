f = open('practice\myfile1.txt','r')
count = 0
data= f.read()
f.close()
for i in range(len(data)):
    if data[i:i+5].lower()=='india':
        count+=1
print("Frequency of India is ", count)