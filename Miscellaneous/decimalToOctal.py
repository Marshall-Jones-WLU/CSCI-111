"""
Author: Marshall Jones
File name: decimalToOctal.py
This file converts decimal integers to base eight, or octal integers.
"""
'''
decimal = int(input("Enter a decimal integer: "))
if decimal == 0:
    print(0)
else:
    print("Quotient Remainder Octal")
    baseEight = ""
    while decimal > 0:
        remainder = decimal % 8
        decimal = decimal // 8
        baseEight = str(remainder) + baseEight
        print("%5d%8d%12s" % (decimal, remainder, baseEight))
print("The octal representation is", baseEight)
'''

"""
For queens.py:
"""

decimal = int(input("Enter a decimal integer: "))
if decimal == 0:
    print(0)
else:
    baseEight = ""
    while decimal > 0:
        remainder = decimal % 8
        decimal = decimal // 8
        baseEight = str(remainder) + baseEight
#baseEight is the variable for the octal representation of the decimal integer.
print("The octal representation is", baseEight)
