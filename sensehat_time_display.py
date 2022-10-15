from sense_hat import SenseHat
import time
import datetime

s = SenseHat()
x = 0
s.set_rotation(180)

try:
	while True:
		now = datetime.datetime.now()
		s.show_message(now.strftime('%I:%M %p'), text_colour = [255,0,0])
		s.clear()
		x += 1
		time.sleep(.50)

except KeyboardInterrupt:
	s.clear()
	pass
