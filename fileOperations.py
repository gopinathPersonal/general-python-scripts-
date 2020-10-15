my_file = open(r"C:\Users\Lakshmi\sample.txt")
print(my_file.read())
# after reading the file the cursor will be at end of the file (EOF)
# to bring back to start of the file
my_file.seek(0) 
print(my_file.read())

# to read a line
my_file.seek(0) 
print(my_file.readline())   # read a single line
my_file.seek(0) 

print(my_file.readlines()) # read all the lines and return in list

my_file.close()  # close the file 