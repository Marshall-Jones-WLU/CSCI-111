"""
Author: Marshall Jones
File name: randomIntegers.py
Description:
This program uses uses functions of the codes created in
random_writer.py and random_reader.py to generate files with
random numbers, and then it reads them, displaying the number
of integers in the file, their average, their maximum value,
and their minimum value.
"""
import random


def writer(name, upper, n):
    f = open(name + ".txt", 'w')
    for t in range(n):
        number = random.randint(1, upper)
        f.write(str(number) + " ")
        if t == n:
            break
    f.close()


def reader(name, upper, n):
    f = open(name + ".txt", 'r')
    theSum = 0
    count = 0
    numbers = []
    for line in f:
        numberList = line.split()
        for num in numberList:
            number = int(num)

            count += 1
            theSum += number
            numbers.append(float(num))

    print("\n")
    print("There are ",count," integers in this file.")

    mean = theSum / count
    print("Average Value: ",mean)

    maxInt = max(numbers)
    print("Maximum Value: ",maxInt)
    minInt = min(numbers)
    print("Minimum Value: ",minInt)


def main():
    name = input("What is the name of the file that you'd like to edit? ")
    upper = int(input("What is the largest possible number that you would like to generate? "))
    n = int(input("How many integers do you want to generate? "))
    writer(name, upper, n) #calls the writer function
    reader(name, upper, n) #calls the reader function


if __name__ == "__main__":
    main()
