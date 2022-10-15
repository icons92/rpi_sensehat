from sense_hat import SenseHat
import numpy as np
import datetime

s = SenseHat()
x = 0
s.set_rotation(180)
s.low_light = True
s_speed = 0.1

my_c = []

try:
    while True:
        
        my_c.append(list(np.random.choice(range(256), size=3)))
        now = datetime.datetime.now()
        s.show_message(now.strftime('%I:%M %p'), scroll_speed=s_speed, text_colour = my_c)
        my_c.clear()
	

except KeyboardInterrupt:
	s.clear()
	pass