import pygame, led, sys, os
from pygame.locals import *

""" A very simple arcade shooter demo :)
"""

BLACK = pygame.Color(0,0,0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)

ledDisplay = led.teensy.TeensyDisplay(sys.argv[1])
size = ledDisplay.size()

simDisplay = led.sim.SimDisplay(size)
screen = pygame.Surface(size)

class Spaceship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('sprite', 'spaceship.png'))
        self.rect = self.image.get_rect()
        self.rect.x = 3

    def move(self, x, y):
        self.rect = self.rect.move(x, y).clamp(screen.get_rect())

class Laser(pygame.sprite.Sprite):
    def __init__(self, spaceship):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((2, 1))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.midleft = spaceship.rect.midright

    def update(self, *args):
        _rect = self.rect.move(1, 0)
        # offscreen?
        if not _rect.colliderect(screen.get_rect()):
            self.kill()
        else:
            self.rect = _rect

def main():
    clock = pygame.time.Clock()
    stage = pygame.sprite.Group()
    spaceship = Spaceship()

    stage.add(spaceship)

    movementX = 0
    movementY = 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    movementY = -1
                elif event.key == K_DOWN:
                    movementY = 1
                elif event.key == K_SPACE:
                    stage.add(Laser(spaceship))

            elif event.type == KEYUP:
                if event.key == K_UP or event.key == K_DOWN:
                    movementY = 0



        spaceship.move(movementX, movementY)

        screen.fill(BLACK)
        stage.update()
        stage.draw(screen)
        simDisplay.update(screen)
        ledDisplay.update(screen)

        clock.tick(30)

main()