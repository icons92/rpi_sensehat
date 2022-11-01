import numpy as np
from sense_hat import SenseHat
from datetime import datetime

import time

s = SenseHat()
s.set_rotation(180)

alarm = datetime.strptime("12:13PM", '%I:%M%p').strftime('%I:%M%p')
a_trigger = False
black = [0,0,0]

try:
    
    sunrise = []
    for i in range(0,64):
           
        sunrise.append([255,205,93])

    while True:
	
	print(sunrise)
	time.sleep(10)
        now = datetime.now().strftime('%I:%M%p')

        if now == alarm:
            a_trigger = True         
            s.set_pixels(sunrise)
        elif now > alarm:            
            pass
        elif now < alarm:            
            pass

        if a_trigger:
            s.show_message(now, text_colour= black, back_colour= sunrise)
        
        
    
except KeyboardInterrupt:
   	
    s.clear()
    pass
