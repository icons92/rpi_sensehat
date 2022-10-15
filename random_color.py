import numpy as np
from sense_hat import SenseHat

import time

s = SenseHat()
s.set_rotation(180)

try:
    while True:
        logo = []
        for i in range(0,64):
            
            logo.append(list(np.random.choice(range(256), size=3)))

        print(logo)
        s.set_pixels(logo)
        time.sleep(1)
        logo.clear()
    
except KeyboardInterrupt:
   	
    s.clear()
    pass
