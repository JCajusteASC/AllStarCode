from Myro import *
init("sim")

def J():
    penDown()
    turnBy(-180,"deg")
    motors(0,1,10)
    forward(1,3)
    penUp()
    turnBy(-90,"deg")
    forward(1,3)

def C():
    penUp()
    motors(1,0,5)
    penDown()
    rotate(1,6)
    motors(1,0,15)

backward(1,5)
turnBy(-90,"deg")
forward(1,4.5)
turnBy(90,"deg")
forward(1,4)
turnBy(90,"deg")
forward(1,5)
J()
turnBy(90,"deg")
backward(1,4)
C()



