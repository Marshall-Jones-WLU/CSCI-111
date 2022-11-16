"""
Author: Marshall Jones
Project 3
File: decipher.py

This program prompts the user to input a password and a secret message,
and it encrypts the message. The user can only reveal their secret
message by typing in their password as the secret key.
"""

key = input("Please enter a new password: ")
message = input("Type your secret message here: ")

for i in range(len(message)):
    k = (ord(key[i % len(key)]) - 97)
    m = (ord(message[i]) - 97)

    codeMessage = chr(((k + m) % 26) + 97)
    print(codeMessage)
