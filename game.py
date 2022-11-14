from sense_hat import SenseHat
from random import randrange

s = SenseHat()

class Player():
    def __init__(self, x, y, color) -> None:
        self.x = x
        self.y = y
        self.color = color
    
    def moveplayer(self, direction):
        #take stick input and move player
        if direction == 'left':
            if self.x > 0:
                self.x -= 1
        elif direction == 'right':
            if self.x > 6:
                self.x += 1
        elif direction == 'up':
            if self.y > 0:
                self.y -= 1
        elif direction == 'down':
            if self.y > 6:
                self.y += 1


class Target():
    def __init__(self) -> None:
        self.x = randrange(7)
        self.y = randrange(7)
        self.color = [randrange(50,256),randrange(50,256),randrange(50,256)]


def updatepixel(obj):
    s.set_pixel(obj.x, obj.y, obj.color)


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
                # Skip releases
                if event.action != "released":
                    if event.direction == "left":
                        updatepixel(player)
                        player.moveplayer('left')
                        updatepixel(player)
                    elif event.direction == "right":
                        updatepixel(player)
                        player.moveplayer('right')
                        updatepixel(player)
                    elif event.direction == "up":
                        updatepixel(player)
                        player.moveplayer('up')
                        updatepixel(player)
                    elif event.direction == "down":
                        updatepixel(player)
                        player.moveplayer('down')
                        updatepixel(player)

    except KeyboardInterrupt:
        s.clear()
        print('\n')
        quit()
        