"""
Author: Marshall Jones
CSCI 111 Final Exam
Filename: pledge.py

This program creates a file called myPledge.txt, containing the text of the
pledge and my name as a signature. It then checks the file's contents and
opens/displays the full text of the file. It also displays the total number
of letters in the file.
"""
def createPledgeFile():
    '''Writes a new file called myPledge.txt with a pledge and signature'''
    pledge = "On my honor, I have neither given nor received any unacknowledged aid on this exam."
    sig = "Marshall Jones"
    Name = "myPledge"
    f = open(Name + ".txt", 'w')
    f.write(pledge + "\n" + sig)
    f.close()

    return Name

def checkPledgeFile(Name):
    '''Reads the file created by createPledgeFile() and prints its text'''
    f = open(Name + ".txt", 'r')
    for line in f:
        print(line)

def countCharacters(Name):
    '''Reads the file created by createPledgeFile() and prints its number
    of letters'''
    f = open(Name + ".txt", 'r')
    count = 0
    wordList = []
    for line in f:
        words = line.split()
        wordList.extend(words)
        for i in wordList:
            jumble = ''.join(wordList)
    jumble = jumble.replace(".", "")
    jumble = jumble.replace(",", "")
    letters = len(jumble)

    #print("Jumble: ",jumble)
    print("\n" + "-"*70 + "\n")
    print("There are " + str(letters) + " letters in the file.")

def main():
    '''Entry point for the program'''
    Name = createPledgeFile()
    checkPledgeFile(Name)
    countCharacters(Name)

if __name__ == "__main__":
    main()
