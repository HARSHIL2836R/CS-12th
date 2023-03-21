# %%
f = open('practice\myfile1.txt','r')
count = 0
data= f.read()
f.close()
####################################
data_words = []
temp = ''
for char in data:
    if char in (' ', ',','.',"'",'"'):
        data_words.append(temp)
        temp =''
    else:
        temp += char
#print(data_words)
#####################################
'''
or use:
import re
data = re.split(', |. ', data)
print(data)
'''
for word in data_words:
    if word.isalpha() and word.lower() == 'india':
        count+=1
print("Frequency of India is ", count)