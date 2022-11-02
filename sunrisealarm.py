import numpy as np
from sense_hat import SenseHat
from datetime import datetime

import time

s = SenseHat()
s.set_rotation(180)
t_in = input('Time as HH:MMPM\n')

alarm = datetime.strptime(t_in, '%I:%M%p').strftime('%I:%M%p')
a_trigger = False
black = [0,0,0]
color = [255,205,93]


try:   

    while True:	
	            
        time.sleep(1)
        now = datetime.now().strftime('%I:%M%p')

        if now == alarm:
            a_trigger = True            
        
        if a_trigger:
            s.show_message(now, text_colour=black, back_colour=color)
        
        for event in s.stick.get_events():
            if event.action != "released":
                print('event happened')
                s.clear()
                quit()
    
except KeyboardInterrupt:
   	
    s.clear()
    pass
