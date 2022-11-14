from sense_hat import SenseHat
import time
from random import randrange

s = SenseHat()
playerl = None
targetl = None
tcolor = None
pcolor = None
    

def target():
    #randomly place a target location with a random color
    tcolor = [randrange(50,256),randrange(50,256),randrange(50,256)]
    x = randrange(7)
    y = randrange(7)    
    s.set_pixel(x,y,tcolor)
    targetl = (x,y)    


def gcheck():
    if playerl == targetl:
        s.set_pixel(playerl[0], playerl[1], tcolor)
        target()

def move(direction):
    #take stick input and move player
    if direction == 'left':
        for x, y in playerl:
            if x > 0:                
                s.set_pixel(x-1,y,pcolor)
                s.set_pixel(x,y,0,0,0)
                playerl = (x-1, y)
                gcheck()
        
    elif direction == 'right':
        for x, y in playerl:
            if x > 6:                
                s.set_pixel(x+1, y, pcolor)
                s.set_pixel(x,y,0,0,0)
                playerl = (x+1, y)
                gcheck()
        
    elif direction == 'up':
        for x, y in playerl:
            if y > 0:                
                s.set_pixel(x, y-1, pcolor)
                s.set_pixel(x, y, 0,0,0)
                playerl = (x, y-1)
                gcheck()
        
    elif direction == 'down':
        for x, y in playerl:
            if y > 6:                
                s.set_pixel(x,y+1,pcolor)
                s.set_pixel(x,y,0,0,0)
                playerl = (x+1, y)
                gcheck()

def start():
    #create starting state for the game
    s.clear()
    s.set_pixel(3,3,255,255,255)
    target()
    playerl = (3,3)

if __name__ == '__main__':

    #run main
    start()    

    try:
        while True:            
            events = s.stick.get_events()
            for event in events:
                # Skip releases
                if event.action != "released":
                    if event.direction == "left":
                        move('left')
                        print('left')
                    elif event.direction == "right":
                        move('right')
                        print('right')
                    elif event.direction == "up":
                        move('up')
                        print('up')
                    elif event.direction == "down":
                        move('down')
                        print('down')

    except KeyboardInterrupt:
        s.clear()
        print('\n')
        quit()
        