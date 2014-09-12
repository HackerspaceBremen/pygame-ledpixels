import pygame, led, sys, os, random
from pygame.locals import *

""" A very simple arcade shooter demo :)
"""

random.seed()

BLACK = pygame.Color(0,0,0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)

ledDisplay = led.teensy.TeensyDisplay(sys.argv[1])
size = ledDisplay.size()
#size = (90, 20)

alienFrequency = 2000
alienSpeed = 0.01

# every time an alien spawns...
alienSpeedFactor = 1.01
alienFrequencyFactor = 1.02

simDisplay = led.sim.SimDisplay(size)
screen = pygame.Surface(size)

class Animation:
    def __init__(self):
        self._lastMove = pygame.time.get_ticks()

    def linearMove(self, x, y, speed):
        distance = (pygame.time.get_ticks() - self._lastMove) * speed
        if distance >= 1:
            self._lastMove = pygame.time.get_ticks()
            return self.rect.move(x * distance, y * distance)

        return self.rect

class Spaceship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('sprite', 'spaceship.png'))
        self.rect = self.image.get_rect()

        self.rect.midleft = screen.get_rect().midleft
        self.rect.x = 3

    def move(self, x, y):
        self.rect = self.rect.move(x, y).clamp(screen.get_rect())

class Alien(pygame.sprite.Sprite, Animation):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        Animation.__init__(self)

        self.image = pygame.image.load(os.path.join('sprite', 'alien.png'))
        self.rect = self.image.get_rect()
        self.rect.midright = screen.get_rect().midright

        self.rect.y = random.randint(0, screen.get_rect().height - self.rect.height)

    def update(self, *args):
        _rect = self.linearMove(-1, 0, alienSpeed)

        if not _rect.colliderect(screen.get_rect()):
            self.kill()
        else:
            self.rect = _rect


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
    global alienSpeed, alienFrequency

    clock = pygame.time.Clock()

    spaceship = Spaceship()
    player = pygame.sprite.Group()
    player.add(spaceship)

    shots = pygame.sprite.Group()
    aliens = pygame.sprite.Group()

    movementX = 0
    movementY = 0
    lastAlien = 0

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
                    shots.add(Laser(spaceship))

            elif event.type == KEYUP:
                if event.key == K_UP or event.key == K_DOWN:
                    movementY = 0

        spaceship.move(movementX, movementY)
        if (pygame.time.get_ticks() - lastAlien) > alienFrequency:
            # spawn new alien :)
            aliens.add(Alien())
            lastAlien = pygame.time.get_ticks()
            alienSpeed *= alienSpeedFactor
            alienFrequency /= alienFrequencyFactor

        # check collisions
        # .. any alien hit?
        pygame.sprite.groupcollide(shots, aliens, True, True)

        # .. player hit?
        alien = pygame.sprite.spritecollideany(spaceship, aliens)

        if alien != None:
            screen.fill(RED)
            alien.kill()
        else:
            screen.fill(BLACK)

        player.update()
        shots.update()
        aliens.update()

        player.draw(screen)
        shots.draw(screen)
        aliens.draw(screen)

        simDisplay.update(screen)
        ledDisplay.update(screen)

        clock.tick(30)

main()