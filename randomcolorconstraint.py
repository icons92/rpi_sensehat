from random import randrange
from sense_hat import SenseHat

import time

s = SenseHat()
s.set_rotation(180)

def red():
    #pick a red color
    r = randrange(256)
    return [r,0,0]
def blue():
    #pick a blue color
    b = randrange(256)
    return [0,0,b]
def green():
    #pick a green color
    g = randrange(256)
    return [0,g,0]

colors = [red, blue, green]

try:
    
    logo = []
    for i in range(0,64):
           
        logo.append(colors[randrange(3)]())

    while True:
       
        #print(logo)
        s.set_pixels(logo)
        time.sleep(.5)
        logo.pop()
        logo.insert(0, colors[randrange(3)]())
    
except KeyboardInterrupt:
   	
    s.clear()
    pass
