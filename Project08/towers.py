"""
Authors: Marshall Jones, Eric Dyer, Johnny Lavette
File: towers.py
Project 8

This program draws each step of the solution to the Tower of Panoi problem.
"""
from images import Image


THICKNESS = 9 #The thickness of the discs
WIDENESS = 31 #The wideness multiplier for each disc. For example, disc 5 is 5*30 wide.
DIMENSIONS = [750,300] #The dimensions for the image
MOVECOUNT = [0]     #The number of moves made
DISC_COLOUR = [0,255,255]

def drawRectangle(img, x1,y1, x2,y2, color = (0,0,0)):
    '''Function draws a rectangle with corners x1,y1 and x2,y2'''
    for x in range(x1, x1 + (x2 - x1)):
        for y in range(y1, y1 + (y2 - y1)):
            img.setPixel(x, y, (color))
    pass

def drawGraphic(tower):
    img = Image(DIMENSIONS[0],DIMENSIONS[1])
    
    # draw ground
    drawRectangle(img, 0,(DIMENSIONS[1]-60), DIMENSIONS[0],(DIMENSIONS[1]-50))
    
    # draw pegs
    pegSpread = DIMENSIONS[0] // 4
    
    drawRectangle(img, (pegSpread),(DIMENSIONS[1]-160), (pegSpread + 10),(DIMENSIONS[1]-60))
    drawRectangle(img, (pegSpread*2),(DIMENSIONS[1]-160), ((pegSpread*2) + 10),(DIMENSIONS[1]-60))
    drawRectangle(img, (pegSpread*3),(DIMENSIONS[1]-160), ((pegSpread*3) + 10),(DIMENSIONS[1]-60))
    
    # draw a bunch of discs according to the list tower
    for p in range(len(tower)):
        lenPeg = len(tower[p])
        for n in range(lenPeg):
            disc = tower[p][n]
            drawRectangle(img, (pegSpread*(p+1) - disc*WIDENESS//2 + 5), (240-(THICKNESS+THICKNESS*n)),
                          (pegSpread*(p+1) + (disc*WIDENESS)//2 + 5), (240-THICKNESS*n),
                          (DISC_COLOUR[0],DISC_COLOUR[1],DISC_COLOUR[2]))

    movecountstring = "{:04}.gif".format(MOVECOUNT[0])      #Filename to save the result in
    print("Drawing Tower", movecountstring, "with config:", tower)
    img.draw()
    img.save("Drawing Tower_" + movecountstring)
    
def moveDisc(tower,src,dest):
    '''
    Move the top disc from the src peg to the destination peg
    pegs is the graphical location of the pegs
    
    YOU PROBABLY DO NOT HAVE TO MESS WITH THIS!!!!
    '''
    
    source = tower[src] #Finds the list to move from
    destination = tower[dest] #Finds the list to move to
    
    disc = source.pop() #Takes the disc off the top of source
    destination.append(disc) #Puts it at the top of destination
    
    MOVECOUNT[0]+=1 #Increments the movecount
    drawGraphic(tower) #TODO draw a picture of what tower looks like
    
def solveTower(tower, n, src, dest, temp):
    '''
    This function moves n discs from src to dest.
    tower is the list which represent the 3 towers
    n is the number of discs to move from src to dest
    temp is the temporary tower to use
    pegs are the graphical locations (x-coordinates) of the pegs
    
    
    Students probably do not need to mess with this fuction!
    Most work should be in moveDisc()
    '''
    if n<=0:
        return
    else:
        solveTower(tower, n-1,src,temp,dest)
        moveDisc(tower, src,dest)
        solveTower(tower, n-1,temp,dest,src)

def towers(height = 6):
    startingTower = [list(range(height,0,-1)),[],[]] #Starting discs
    drawGraphic(startingTower)
    solveTower(startingTower, height, 0, 2, 1) #Move all discs from peg 0 to peg 2, with peg 1 as the temporary peg.

if __name__ == "__main__":
    towers(6)
    input("Press Enter to Quit")
