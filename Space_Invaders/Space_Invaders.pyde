from time import sleep

def setup():
    
    size(600,600)
    background(0)


aliens = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
xA = 75
yA = 75
x = 300
xB = 0
yB = 527
counter = 0
a1 = 30
b1 = 58
c1 = 86
shield = 0

isBulletFired = False

def draw():
    global x, xA, yA,yB, isBulletFired, xB, shield, a1, b1, c1
    ellipseMode(CENTER)
    background(0)
    rectMode(CENTER)
    rect(x, 550,50, 25)
    fill(0,255,0)
    
    
    triangle(a1+50, 475, b1+50, 420, c1+50, 475);  
    triangle(a1+150, 475, b1+150, 420, c1+150, 475);  
    triangle(a1+250, 475, b1+250, 420, c1+250, 475);  
    triangle(a1+350, 475, b1+350, 420, c1+350, 475);  
    triangle(a1+450, 475, b1+450, 420, c1+450, 475);  

        
    if x > 550:
        x = x + 0
    if keyPressed and key == "d": #right
        x = x + 5
        
    
    if keyPressed and key == "a": #left
        x = x - 5
        
    bullet  = [[xB,yB],[xB,yB],[xB,yB],[xB,yB]]
    if bullet > 500:
        bullet.append([xB,yB])
  
    if keyPressed and key == " " and isBulletFired == False: #if space pressed and no bullet fired
        isBulletFired = True
        xB = x #Make position of bullet be the current position of ship
            
    if isBulletFired == True:
        rect(xB, yB, 2, 20)
        yB = yB - 5
    if yB < 75:
        yB = 527
        isBulletFired = False

    
    for i in range(len(aliens)):
            for j in range(len(aliens[i])):
                if aliens[i][j] == 0:
                    ellipse(i*75 + 150, j*75 + 50, 50, 50)        
                if yB == j*100+50 and xB == i*100+100:
                    aliens.pop([i][j])
                        
    
            
    
        
    
    
        

        

        
    