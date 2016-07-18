from random import *

def setup():
    size(500, 500)
    background(155, 125, 205);
    noStroke();
    
def draw():
    rect(100, 0, 100, 100);
    fill(0, 0, 0)
    rect(0, 0, 100, 100);
    fill(0, 0, 0)
    #if (mouseX < 100):
    ellipse(mouseX, mouseY, 15, 15);
    fill(0, 0, 255)
        
    rect(100, 0, 100, 100);
    fill(0, 0, 255)
    #if (100 < mouseX < 200):
    ellipse(mouseX, mouseY, 15, 15);
    fill(255,0,0)
        
    rect(200, 0, 100, 100);
    fill(255, 0,0)
    #if (200 < mouseX < 300):
    ellipse(mouseX, mouseY, 15, 15);
    fill(0,255,0)
        
    rect(300, 0, 100, 100);
    fill(0, 255, 0)
   # if (300 < mouseX < 400):
    ellipse(mouseX, mouseY, 15, 15);
    fill(255, 255, 0)
        
    rect(400, 0, 100, 100);
    fill(255, 255,0)
    ellipse(mouseX, mouseY, 15, 15);
       
#'0-100
#100-200
#200-300
#300-400'

#black
#blue
#red
#green
#yellow
#green
#yellow