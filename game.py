from sense_hat import SenseHat
from random import randrange

s = SenseHat()

class Player():
    def __init__(self, x, y, color) -> None:
        self.x = x
        self.y = y
        self.color = color
        self.score = 0

    def moveplayer(self, direction):
        #take stick input and move player
        self.color = [255,255,255]
        print(direction)
        print(self.x, self.y)
        if direction == 'left':
            if self.x > 0:
                self.x -= 1
                
        elif direction == 'right':
            if self.x < 6:
                self.x += 1
                
        elif direction == 'up':
            if self.y > 0:
                self.y -= 1
                
        elif direction == 'down':
            if self.y < 6:
                self.y += 1
                


class Target():
    def __init__(self) -> None:
        self.x = randrange(7)
        self.y = randrange(7)
        self.color = [randrange(50,256),randrange(50,256),randrange(50,256)]


def updatepixel(obj):
    s.set_pixel(obj.x, obj.y, obj.color)

def goal(tobj, pobj):
    if tobj.x == pobj.x and tobj.y == pobj.y:        
        tobj.x = randrange(7)
        tobj.y = randrange(7)
        tobj.color = [randrange(50,256),randrange(50,256),randrange(50,256)]
        pobj.score += 1        


if __name__ == '__main__':
    
    s.clear
    

    player = Player(3,3,[255,255,255])
    updatepixel(player)
       
    target = Target()
    updatepixel(target)

    try:
        while True:
            events = s.stick.get_events()
            for event in events:
                player.color = [0,0,0]
                # Skip releases
                if event.action != "released":
                    if event.direction == "left":
                        updatepixel(player)
                        player.moveplayer('left')
                        updatepixel(player)
                        goal(target, player)
                    elif event.direction == "right":
                        updatepixel(player)
                        player.moveplayer('right')
                        updatepixel(player)
                        goal(target, player)
                    elif event.direction == "up":
                        updatepixel(player)
                        player.moveplayer('up')
                        updatepixel(player)
                        goal(target, player)
                    elif event.direction == "down":
                        updatepixel(player)
                        player.moveplayer('down')
                        updatepixel(player)
                        goal(target, player)
                    elif event.direction == "middle":
                        s.set_rotation(180)
                        message = 'Good game you scored' + str(player.score) + 'points!'
                        s.show_message(message)
                        s.clear()
                        quit()
                        

    except KeyboardInterrupt:
        s.clear()
        print('\n')
        quit()
        