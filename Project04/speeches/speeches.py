"""
Author: Marshall Jones
File name: speeches.py
This program performs analysis for each .txt file in its folder.
For each file, it displays the name of the file, the longest
word in the file, the average word length in the file, and the
longest sentence in the file.
"""

'''
What I need to know:
- name of each file
- longest word in each file
- average word length in each file:
    - number of letters / number of words
- longest sentence in each file
'''

import os

def main():
    files = os.listdir()
    real_files = []
    for name in files:
        if name.endswith(".txt"):
            real_files.append(name)

    for name in real_files:
        reader(name, real_files)


def reader(name, real_files):
    file = open(name, 'r')
    speech = ""
    while True:
        line = file.readline()
        wordList = []
        speech += line
        if line == '':
            break  

    wordList = speech.split()
    nWords = len(wordList)
    TotalLetters = 0
    longestWord = ""
    for x in wordList:
        wordLength = len(x)
        if len(longestWord) < len(x):
            longestWord = x
        
        TotalLetters += wordLength
    avgWordLen = round((TotalLetters / nWords),2)


    sentenceList = speech.split("." or "!" or "?")
    longestSentence = ""
    for sentence in sentenceList:
        sentenceLength = len(sentence)
        if len(longestSentence) < len(sentence):
               longestSentence = sentence

    
    print("File name: ",name)
    print("The longest word is ",'"' + longestWord + '"')
    print("The average word length is",str(avgWordLen) + ".")
    print("The longest sentence is: ", longestSentence)
    print("\n"*2)


if __name__ == "__main__":
    main()
