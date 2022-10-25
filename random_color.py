import numpy as np
from sense_hat import SenseHat

import time

s = SenseHat()
s.set_rotation(180)

try:
    
    logo = []
    for i in range(0,64):
           
        logo.insert(0,list([0,0,0]))

    while True:
       
        print(logo)
        s.set_pixels(logo)
        time.sleep(1)
        logo.pop()
        logo.insert(0,list(np.random.choice(range(256), size=3)))
    
except KeyboardInterrupt:
   	
    s.clear()
    pass
