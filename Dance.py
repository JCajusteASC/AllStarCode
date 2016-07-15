from Myro import * 
init("sim") 

counterclock = 4
clock = 4 
counterclock2 = 4

while counterclock < 5:
    motors(0,1,21)
    counterclock = counterclock + 1
rotate(1,3)
while clock < 5:
    motors(1,0,21)
    clock = clock + 1  
rotate(1,3) 
while counterclock2 < 5:
    motors(0,1,21)
    counterclock2 = counterclock2 + 1
rotate(1)