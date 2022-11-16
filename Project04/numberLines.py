"""
Author: Marshall Jones
File name: numberLines.py
This program numbers the lines of text in a file. It first prompts
the user to enter a file name. The program then outputs a new numbered
file with a new name.
"""
def main():
    import os

    filename = input("What is the filename? ")
#    file = open("/Users/marshalljones/Desktop/Python 1/Project4/" + filename,'r')
    file = open(filename,'r')

    count = 0

    while True:
#        numberedFile = open("/Users/marshalljones/Desktop/Python 1/Project4/" + "numbered" + filename,'a')
        numberedFile = open("numbered" + filename,'a')
        line = file.readline()
        numberedFile.write(str(count) + "  " + line)
        count += 1
        if line == "":
            break

    numberedFile.close()

if __name__ == "__main__":
    main()
