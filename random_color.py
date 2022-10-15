from curses import KEY_A1
import numpy as np
from sense_hat import SenseHat

import time

s = SenseHat()
s.set_rotation(180)

try:
    while True:
        logo = []
        for i in range(0,63):
            print(i)
            logo.append(list(np.random.choice(range(256), size=3)))

        s.set_pixel(logo)
        time.sleep(1)
        logo.clear()
    
except KeyboardInterrupt:
   	
    s.clear()
    pass
