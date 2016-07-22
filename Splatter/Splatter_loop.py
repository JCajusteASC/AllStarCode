from random import choice

def setup():
    size(500, 500)
    background(155, 125, 205);
    noStroke();
    
def draw():
    ellipse(mouseX+randint, mouseY+randint, 55, 55);
    fill( random(255), random(255), random(255), random(255));
    