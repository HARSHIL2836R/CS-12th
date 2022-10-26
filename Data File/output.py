f= open("myfile.txt", "w+")
print ("Name of the file: ", f.name)
# Assuming that the file contains these lines
# TechBeamers
# Hello Viewers!!
seq="Python programming\nHello Programmers!!"
f.writelines(seq )

f.seek(0,0)
for line in f:
    print (line)
f.close()