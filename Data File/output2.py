# Open a file in read-write mode
f = open("myfile.txt", "w+")
print ("Name of the file: ", f.name)
# Assuming file has the following line
txt = "This is 1st line of text file,"
f.writelines( txt )
seq = " This is 2nd line, This is 3rd line of text file"
# Write sequence of lines at the end of the file.
f.seek(0, 2)
f.writelines( seq )
# Now read complete file from beginning.
f.seek(0,0)
line = f.readlines()
print ("Read Line: %s" % (line))
# Close the file
f.close()
input()
