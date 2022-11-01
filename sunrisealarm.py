import numpy as np
from sense_hat import SenseHat
from datetime import datetime

import time

s = SenseHat()
s.set_rotation(180)
t_in = input('Time as HH:MMPM\n')

alarm = datetime.strptime(t_in, '%I:%M%p').strftime('%I:%M%p')
a_trigger = False
black = []
black.append(0)
black.append(0)
black.append(0)

sunrise = []
for i in range(0,64):
           
    sunrise.append([255,205,93])

try:   

    while True:	
	    
        
        time.sleep(1)
        now = datetime.now().strftime('%I:%M%p')

        if now == alarm:
            a_trigger = True            
        elif now > alarm:            
            pass
        elif now < alarm:            
            pass

        if a_trigger:
            s.show_message(now, text_colour=black, back_colour=sunrise)
        
        
    
except KeyboardInterrupt:
   	
    s.clear()
    pass
