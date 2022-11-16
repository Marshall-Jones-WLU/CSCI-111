"""
Author: Marshall Jones, Eric Dyer, and Johnny Lavette
File: testimage.py
Project 8

Script for testing image processing functions.
"""
# import libraries
from images import Image
import random

# Functions that transform images
def blackAndWhite(image):
    """Converts image to black and white."""
    blackPixel = (0, 0, 0)
    whitePixel = (255, 255, 255)
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            average = (r + g + b) // 3
            if average < 128:
                image.setPixel(x, y, blackPixel)
            else:
                image.setPixel(x, y, whitePixel)

def posterize(image, color):
    """Converts image to either that color or white"""
    blackPixel = color
    whitePixel = (255, 255, 255)
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            average = (r + g + b) // 3
            if average < 128:
                image.setPixel(x, y, blackPixel)
            else:
                image.setPixel(x, y, whitePixel)

def sepia(image):
    """Converts image to sepia"""
    blackPixel = (0, 0, 0)
    whitePixel = (255, 255, 255)

    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            red = r
            blue = b
            if red < 63:
                red = int(red*1.1)
                blue = int(blue*0.9)
                image.setPixel(x, y, (red, g, blue))
                
            elif red < 192:
                red = int(red*1.15)
                blue = int(blue*0.85)
                image.setPixel(x, y, (red, g, blue))
                
            else:
                red = min(int(red*1.08), 255)
                blue = int(blue*0.93)
                image.setPixel(x, y, (red, g, blue))

def rotateRight(image):
    '''Rotates image 90 degrees clockwise'''
    newImage = Image(image.getHeight(), image.getWidth())
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            height = image.getHeight()
            (r, g, b) = image.getPixel(x, y)
            newImage.setPixel(height-y, x, (r, g, b))
    newImage.draw()

def colorscale(image, targColor = (0,0,0)):
    '''Converts image to colorscale'''
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (red, green, blue) = image.getPixel(x, y)
            bright = (red*0.299 + green*0.587 + blue*0.114)/255
            r = int((255-targColor[0])*bright+targColor[0])
            g = int((255-targColor[1])*bright+targColor[1])
            b = int((255-targColor[2])*bright+targColor[2])
            image.setPixel(x, y, (r, g, b))

# Tester functions
def testBlackAndWhite(name = "smokey.gif"):
    """Loads and draws an image, then
    converts it to black and white and redraws it."""
    image = Image(name)
    print("Close the image window to see the transformation. This may take a few seconds.")
    image.draw()
    blackAndWhite(image)
    image.save("blackAndWhite_" + name)
    image.draw()

def testPosterize(name = "smokey.gif"):
    """Loads and draws an image, then
    converts the colors to achieve a sepia effect and redraws it."""
    image = Image(name)
    color = ((random.randint(0,255)), (random.randint(0, 255)), (random.randint(0, 255)))
    print("Close the image window to see the transformation. This may take a few seconds.")
    image.draw()
    posterize(image, color)
    image.save("posterize_" + name)
    image.draw()

def testSepia(name = "smokey.gif"):
    """Loads and draws an image, then
    converts it to black and white and redraws it."""
    image = Image(name)  
    print("Close the image window to see the transformation. This may take a few seconds.")
    image.draw()
    sepia(image)
    image.save("sepia_" + name)
    image.draw()

def testRotateRight(name = 'mouse.gif'):
    '''Loads and draws an image, then
    rotates it 90 degrees clockwise and redraws it.'''
    image = Image(name)
    image.draw()
    rotateRight(image)
    image.save("rotateRight_" + name)

def testColorscale(name = 'mouse.gif'):
    '''Loads and draws an image, then
    scales the colors between a target color and white and redraws it.'''
    image = Image(name)
    image.draw()
    colorscale(image, (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    image.save("colorscale_" + name)
    image.draw()

# main and name functions
def main(name = "mouse.gif"):
    name = input("What is the name of the image you would like to edit? ")
    print("Now testing blackAndWhite..")
    testBlackAndWhite(name)
    print("Now testing posterize..")
    testPosterize(name)
    print("Now testing sepia..")
    testSepia(name)
    print("Now testing rotateRight..")
    testRotateRight(name)
    print("Now testing colorscale..")
    testColorscale(name)
    print("Program completed.")

if __name__ == "__main__":
    main()
    #main("mouse.gif")
    #main("penguin.gif")
    #main("planet.gif")
    #main("smokey.gif")
        
