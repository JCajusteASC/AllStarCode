from time import *
from random import *

speedX = 1
speedY = 1
moveX = 256
moveY = 246
moveX2 = 50
moveY2 = 50
speedX2 = 1
speedY2 = 1


def setup():
    
    size(500,500)
    background(155, 125, 205);
    noStroke()
    
    
def draw():
    global speedX
    global speedY
    global moveX
    global moveY
    global speedX2
    global speedY2
    global moveX2
    global moveY2
    moveX2 = moveX2 + speedX2
    moveY2 = moveY2 + speedY2
    moveX= moveX + speedX
    moveY = moveY + speedY
    
    background(155, 125, 205);
    ellipse(moveX, moveY, 55, 55);
    fill(0,255,0)
    
    if moveX > 480:
        speedX = speedX * -1
        
    if moveY > 480:
        speedY =speedY * -1
        
    if moveX < 20:
        speedX =speedX * -1
        
    if moveY < 20:
        speedY = speedY * -1
        
    if moveY > mouseX and moveY < 90:
        speedY = speedY * -1
    
    
    rect(mouseX, 50, 100, 50)
    fill(255,0,0)
    
    if moveX2 > 500:
        speedX2 = speedX2 * -1
        
    if moveX2 < 200:
        speedX2 = speedX2 * -1
        

   
    