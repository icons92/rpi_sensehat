import numpy as np
from sense_hat import SenseHat
import datetime

import time

s = SenseHat()
s.set_rotation(180)

try:
    
    sunrise = []
    for i in range(0,64):
           
        sunrise.insert(0,list([247,205,93]))

              
    s.set_pixels(sunrise)
    
        
        
    
except KeyboardInterrupt:
   	
    s.clear()
    pass
