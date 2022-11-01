import numpy as np
from sense_hat import SenseHat
from datetime import datetime

import time

s = SenseHat()
s.set_rotation(180)

alarm = datetime.strptime("11:45AM", '%I:%M%p').strftime('%I:%M%p')

try:
    
    sunrise = []
    for i in range(0,64):
           
        sunrise.insert(0,list([247,205,93]))

    while True: 

        time.sleep(10)       
        now = datetime.now().strftime('%I:%M%p')

        if now == alarm:         
            s.set_pixels(sunrise)
        elif now > alarm:
            print('now is greater')
            print('{} > {}'.format(now, alarm))
        elif now < alarm:
            print('now is less than alarm')
            print('{} < {}'.format(now, alarm))
        
        
    
except KeyboardInterrupt:
   	
    s.clear()
    pass
