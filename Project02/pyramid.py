'''
Author: Marshall Jones
Project 2
File name: pyramid.py
Description: This program displays a pyramid with a variable height.
'''

h = (int(input("What will be the height of your pyramid? ")))*2

for pyramid in range(1,h+1,2):
    print((" "*((h-pyramid)//2))+str((pyramid)*"#"))

