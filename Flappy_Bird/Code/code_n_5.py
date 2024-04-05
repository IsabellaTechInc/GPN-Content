from pygame import *
from random import *


init()

background_image = image.load("bg.png")
bird_image = image.load("bird.png")
pipe_image = image.load("pipe.png")
flipped_pipe_image = transform.flip(pipe_image, False, True)
coin_image = image.load("coin.png")

#Made an NPC parent class because of all the similarities in the methods
class NonPlayable():
    def __init(self,x,y,coin):
        seld.x=x
        self.y=y
        self.image=image.load("noImage.png")
        self.coin=coin

    def blit(self):
        self.rect = screen.blit(self.image,(self.x, self.y))

    def move(self):
        #gravity
        self.x = self.x-2
        if self.x<=-70:
            #wrap around
            self.x=800
            self.y= randint(100,500)
            if not self.coin:
                #this replaces self.flipped so it still works with coin inheritance wise (migh be a better way to do this?)
                if choice([True, False]):
                    self.y=-self.y
                    self.image= transform.flip(self.image, False, True)

    def collides_with(self, bird):
        #collated the overall function of the collides (collides_with and collected_by)
        if bird.colliderect(self.rect):
            if self.coin:
                self.x = 800
                self.y = randint(100, 500)
            return True
        return False

class Pipe (NonPlayable):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image=pipe_image
        #this might make the game harder just because it doesn't ensure any initial direction but i figured it was ok
        if choice([True,False]):
            self.y=-self.y
            self.image= transform.flip(self.image, False, True)
        self.coin=False


class Coin (NonPlayable):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image=coin_image
        self.coin=True



init()

print("The game is about to start!")

screen = display.set_mode((800, 600))

background_image = image.load("bg.png")
bird_image = image.load("bird.png")


bird_x = 10
bird_y = 250

pipe1_object = Pipe(200, 250)
pipe2_object = Pipe(450, 100)
pipe3_object = Pipe(700, 400)

pipes = [pipe1_object, pipe2_object, pipe3_object]


coin = Coin(400, 150)

points = 0

over = False

while True:

    new_event = event.poll()
    if new_event.type == KEYDOWN and new_event.key == K_UP:
        bird_y = bird_y - 50
    if new_event.type == KEYDOWN and new_event.key == K_DOWN:
        bird_y = bird_y + 50

    for pipe in pipes:
        pipe.move()

    #Move the coin
    coin.move()


    background = screen.blit(background_image, (0, 0))
    # i know functionality wise bird doesn't need to be a class but it would help teach them?
    bird = screen.blit(bird_image, (bird_x, bird_y))

    for pipe in pipes:
        pipe.blit()

    coin.blit()
        
    display.update()

    for pipe in pipes:
        if pipe.collides_with(bird):
            print("Game Over!")
            quit()
            over = True
            break
        
    #Check if the coin collides
    if coin.collides_with(bird):
        points = points + 1

    if over:
        break

#Print out our point total at the end
print("Points:", points)
