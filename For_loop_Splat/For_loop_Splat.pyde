from random import *

def setup():
    size(500, 500)
    background(155, 125, 205);
    noStroke();
    
def draw():
    x = randrange(5,50)
    color= randrange(150, 255, 50)
    noStroke()
    fill(color)
    ellipse(mouseX, mouseY, x,x)
    for i in range(randrange(15)):
        splatX = randrange(-50,50)
        splatY = randrange(-50,50)
        splatSize = randrange(int(x/4), int(x/2))
        ellipse(mouseX + splatX,mouseY + splatY,splatSize, splatSize)