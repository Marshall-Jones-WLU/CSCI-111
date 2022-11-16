"""
Author: Marshall Jones
File name: random_reader.py
Description:
This program reads random integers from a file created by the program
random_writer.py. It displays the number of integers in the file,
their average, their maximum value, and their minimum value.
"""
name = input("What is the name of the file that you previously created? ")

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
#print("The sum is", theSum)

mean = theSum / count
print("Average Value: ",mean)

maxInt = max(numbers)
print("Maximum Value: ",maxInt)
minInt = min(numbers)
print("Minimum Value: ",minInt)

print("numberList: ",numberList)
