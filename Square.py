from Myro import * # Import all functions from Myro
init("sim") # Start simulator

moveforward=1
time = 1
mf = 2
t = 2

loop=1
loop2=1

while loop < 5:
    forward(moveforward,time)
    turnBy(90,"deg")
    loop = loop + 1
while loop2 < 5:
    forward(mf,t)
    turnBy(90,"deg")
    loop2 = loop2 + 1