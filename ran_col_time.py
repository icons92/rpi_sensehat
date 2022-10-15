from sense_hat import SenseHat
import numpy as np
import datetime

s = SenseHat()
x = 0
s.set_rotation(90)
s.low_light = True
s_speed = 0.1

my_c = []
my_c_inv = []

try:
    while True:
        
        my_c = list(np.random.choice(range(256), size=3))
        now = datetime.datetime.now()
        print(my_c)
        for i in my_c:
            my_c_inv.append(255-i)

        s.show_message(now.strftime('%I:%M %p'), scroll_speed=s_speed, text_colour = my_c, back_colour= my_c_inv)
        my_c.clear()
        my_c_inv.clear()
	

except KeyboardInterrupt:
	s.clear()
	pass