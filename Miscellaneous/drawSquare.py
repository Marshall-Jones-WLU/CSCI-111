from turtle import Turtle

def drawSquare(t, dist=100):
    for i in range(4):
        t.forward(dist)
        t.right(90)

def drawDiamond(t, dist=100):
    t.right(45)
    for i in range(4):
        t.forward(dist)
        t.right(90)

def main():
    t = Turtle()
    drawSquare(t)
    #drawDiamond(t)

if __name__ == "__main__":
    main()
