from random import *

def setup():
    size(500, 500)
    background(155, 125, 205);
    noStroke();
    
def draw():
    rect(0, 0, 100, 100);
    fill(0, 0, 255)
   # if mouseClicked():
    ellipse(mouseX, mouseY, 15, 15);
    rect(100, 0, 100, 100);
    fill(255, 0, 0)
   # if mouseClicked()
    ellipse(mouseX, mouseY, 15, 15);
    rect(200, 0, 100, 100);
    fill(0, 255, 0)
    #if mouseClicked()
    ellipse(mouseX, mouseY, 15, 15);
    rect(300, 0, 100, 100);
    fill(255, 255, 0)
  #  if mouseClicked()
    ellipse(mouseX, mouseY, 15, 15);
    rect(400, 0, 100, 100);
    fill(0, 0, 0)
   # if mouseClicked()
    ellipse(mouseX, mouseY, 15, 15);