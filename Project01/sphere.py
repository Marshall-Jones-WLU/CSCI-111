import math

radius = float(input("Enter the sphere's radius: "))
diameter = radius * 2
circumference = 2 * math.pi * radius
sa = 4 * math.pi * radius ** 2
volume = (4/3) * math.pi * radius ** 3

print("Diamter = " + str(diameter))
print("Circumference = " + str(circumference))
print("Surface Area = " + str(sa))
print("Volume = " + str(volume))
