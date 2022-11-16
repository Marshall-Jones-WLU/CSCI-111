'''
Author: Marshall Jones
Project 2
File name: bouncyBall.py
Description: This program calculates the total distance that a bouncy ball travels in a given number of bounces.
'''

iH = float(input("How high (in feet) are you dropping the ball? "))
b = float(input("What is the bounciness index of the ball? "))
n = int(input("How many times will you allow the ball to bounce? "))

tD = iH

for nb in range(1,n+1):
    bH = iH * (b ** nb)
    tD += 2*bH

print("TOTAL DISTANCE:")
print(round(tD,2))

