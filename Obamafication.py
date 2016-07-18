from Myro import *

Obama_DarkBlue = makeColor(0,51,76)
Obama_Red = makeColor(217, 26, 33)
Obama_Blue = makeColor(112,150,158)
Obama_Yellow = makeColor(252, 227, 166)

#Gray=(Red+Green+Blue)/3

pic = makePicture(pickAFile())

for pixel in getPixels(pic):
    gray = getGray(pixel)
    if (gray > 180):
        setColor(pixel,Obama_Yellow)
    elif (180 > gray > 120):
        setColor(pixel,Obama_Blue)
    elif (120 > gray > 60):
        setColor(pixel,Obama_Red)
    else:
        setColor(pixel,Obama_DarkBlue)   



show(pic)