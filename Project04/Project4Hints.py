import random

name = "test_file.txt"
numbs = 100
max_numb = 2500

f = open(name,'w')
for i in range(numbs):
    j = random.randint(1,max_numb)
    f.write(str(j) + " ")
f.close()

"""
Below is a function of the same code written above:
"""
import random

def main(): #This function is used to create inputs for the user.
    name = input("File? ")
    n = int(input("N? "))
    max_value = int(input("Max? "))
    writer(name, n, max_value) #This line calls the writer function
    reader(name) #This line calls the reader function

#To write a function:
def writer(filename, numbs, max_numb):
    #code
    f = open(filename,'w')
    for i in range(numbs):
        j = random.randint(1,max_numb)
        f.write(str(j) + " ")
    f.close()

"""
It is important to remember that the following 2 lines of code are necessary for
executing the functions.
"""

if __name__ = "__main__":
    main()

"""
To get a list of the file names in a folder, use the following. The following code
may also do something else. Not really sure.
"""

import os

def main():
    files = os.listdir()
    real_file = []
    for name in files:
        if name.endswith(".txt"):
            real_files.append(name)

    for name in real_files:
        reader(name)

"""
Remember that lists are something that can be appended.
append()
<list>.append(<an element>)

