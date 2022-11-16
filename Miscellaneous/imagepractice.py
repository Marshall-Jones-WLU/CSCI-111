from images import Image
m = Image("mouse.gif")
w = m.getWidth()
h = m.getHeight()

for i in range(h):
    for j in range(w):
        current = m.getPixel(i,j)
        average = sum(current)/3
        if average > 128:
            m.setPixel(i,j, (255,255,255))
        else:
            m.setPixel(i,j, (0,0,0))
m.draw()
