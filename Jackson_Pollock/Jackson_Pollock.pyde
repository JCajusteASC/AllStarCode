from random import choice

def setup():
    size(500, 500)
    background(155, 125, 205);
    noStroke();
    
def draw():
    ellipse(mouseX, mouseY, 55, 55);
    fill( random(255), random(255), random(255), random(255));
    ellipse(mouseX-50, mouseY, 45, 45);
    fill( random(255), random(255), random(255), random(255));
    ellipse(mouseX-75, mouseY, 35, 35);
    fill( random(255), random(255), random(255), random(255));
    ellipse(mouseX-100, mouseY, 25, 25);
    fill( random(255), random(255), random(255), random(255));
    ellipse(mouseX, mouseY-50, 45, 45);
    fill( random(255), random(255), random(255), random(255));
    ellipse(mouseX, mouseY-75, 35, 35);
    fill( random(255), random(255), random(255), random(255));
    ellipse(mouseX, mouseY-100, 25, 25);
    fill( random(255), random(255), random(255), random(255));    
    ellipse(mouseX+50, mouseY, 45, 45);
    fill( random(255), random(255), random(255), random(255));
    ellipse(mouseX+75, mouseY, 35, 35);
    fill( random(255), random(255), random(255), random(255));
    ellipse(mouseX+100, mouseY, 25, 25);