import numpy as np
from sense_hat import SenseHat

import time

s = SenseHat()
s.set_rotation(180)

def red():
    #pick a red color
    r = np.random.choice(range(256), size=1)
    return list([r,0,0])
def blue():
    #pick a blue color
    b = np.random.choice(range(256), size=1)
    return list([0,b,0])
def green():
    #pick a green color
    g = np.random.choice(range(256), size=1)
    return list([0,0,g])

colors = [red(), blue(), green()]

try:
    
    logo = []
    for i in range(0,64):
           
        logo.append(np.random.choice(colors, 1))

    while True:
       
        print(logo)
        s.set_pixels(logo)
        time.sleep(1)
        logo.pop()
        logo.insert(0, np.random.choice(colors, 1))
    
except KeyboardInterrupt:
   	
    s.clear()
    pass
