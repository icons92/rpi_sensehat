from sense_hat import SenseHat
import time
import datetime

s = SenseHat()
x = 0
s.set_rotation(180)
s.low_light = True
s_speed = 0.1

index = 0
visual = ['time', 'date']

red = [255,0,0]
green = [0,255,0]
blue = [0,0,255]

c_index = 0
color = [red, green, blue]

def update_screen(m, c):
	if m == 'time':
		now = datetime.datetime.now()
		s.show_message(now.strftime('%I:%M %p'), scroll_speed=s_speed, text_colour = c)
	elif m == 'date':
		now = datetime.datetime.now()
		s.show_message(now.strftime('%x'), scroll_speed=s_speed, text_colour = c)



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
				elif event.direction == "middle":
					c_index += 1
					selection = True	
				if selection:
					current_mode = visual[index % 2]
					color_selected = color[c_index % 3]
					update_screen(current_mode, color_selected)
		
		if not selection:      
			current_mode = visual[index % 2]
			color_selected = color[c_index % 3]
			update_screen(current_mode, color_selected)
	
	

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