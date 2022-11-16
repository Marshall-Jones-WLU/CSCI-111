'''
Author: Marshall Jones
Project 2
File name: pyramid2.py
Description: This program displays a pyramid with a variable height a
variable number of times.
'''

h = (int(input("What will be the height of your pyramid? ")))*2
t = (int(input("How many pyramids would you like to display? ")))

for i in range(t):
    for pyramid in range(1,h+1,2):
        print((" "*((h-pyramid)//2))+str((pyramid)*"#"))

