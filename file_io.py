#File Input/Output

my_list = [i**2 for i in range(1,11)]
# Generates a list of squares of the numbers 1 - 10

f = open("output.txt", "w")
#This told Python to open output.txt in "w" mode ("w" stands for "write"). We stored the result of this operation in a file object, f.
#"r+"  will allow you to read and write  


for item in my_list:
    f.write(str(item) + "\n")

f.close()
#You must close the file.  If you don't close your file, Python won't write to it properly. From here on out, you gotta close your files!

