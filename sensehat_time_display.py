from sense_hat import SenseHat
import time
import datetime

s = SenseHat()
x = 0
s.set_rotation(180)
s_speed = 0.05

index = 0
visual = ['time', 'date']

def update_screen(m):
	if m == 'time':
		now = datetime.datetime.now()
		s.show_message(now.strftime('%I:%M %p'), scroll_speed=s_speed, text_colour = [255,0,0])
	elif m == 'date':
		now = datetime.datetime.now()
		s.show_message(now.strftime('%x'), scroll_speed=s_speed, text_colour = [0,255,0])



try:
	while True:
		selection = False
		events = s.stick.get_events()
		for event in events:
			# Skip releases
			if event.action != "released":
				if event.direction == "left":
					index -= 1
					selection = True
				elif event.direction == "right":
					index += 1
					selection = True
				if selection:
					current_mode = visual[index % 2]
					update_screen(current_mode)
		
		if not selection:      
			current_mode = visual[index % 2]
			update_screen(current_mode)
	
	

except KeyboardInterrupt:
	s.clear()
	pass

'''
while True:
		now = datetime.datetime.now()
		s.show_message(now.strftime('%I:%M %p'), text_colour = [255,0,0])
		s.clear()
		x += 1
		time.sleep(.50)
'''