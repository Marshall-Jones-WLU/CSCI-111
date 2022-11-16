'''
Author: Marshall Jones
Midterm Exam
File name: drawDiamond.py
Description:
This program has one function that takes an input integer, and it displays a
diamond of "$" and "#" with a variable size according to the integer.
I know I can figure this out and get it perfect, but I just need more time.
'''
"""
def drawDiamond(height):
    
    for diamond in range(1, height+1, 2):
        if height == 1:
            print((" "*((height-diamond)//2))+str((diamond)*"$"))
        elif height > 1:
            print((" "*((height-diamond)//2))+str("$"))
            print((" "*((height-diamond)//2))+str((height-1)*"$#" + "$"))
            print((" "*((height-diamond)//2))+str("$"))

drawDiamond(int(input("Enter an integer to display a fun and engaging diamond: ")))
"""
def drawDiamond(height):
    
    diamond = ['$']
    newElements = ['#','$']
    for shape in range(1, height+1, 2):
        While (len(diamond) <= height:
            if height > 1:
                diamond.extend(newElements*(height-1))
            formula = (" "*((height-shape)//2))+str(diamond)
            print((formula + "\n")*height)
        While len(diamond) > height:
            if height < 2:
                break
            else:
                diamond.pop(newElements)
            formula = (" "*((height-shape)//2))+str(diamond)
            print((formula + "\n")*height)

drawDiamond(int(input("Enter an integer to (not) display a fun and engaging diamond: ")))

