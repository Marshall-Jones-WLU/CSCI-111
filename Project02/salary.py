'''
Author: Marshall Jones
Project 2
File Name: salary.py
Description: This program calculates the salaries of elementary school teachers.
'''

starting_salary = float(input("What was your starting salary? "))
r = float(input("What is the yearly percentage increase of your salary? "))
t = int(input("How many years have you been teaching for this school? "))

print("YEAR", "SALARY")

for t in range(0, t):
    salary = round((starting_salary * (1 + (r/100))**t),2)
    print(t,salary)

