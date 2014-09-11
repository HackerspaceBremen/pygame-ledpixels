import sys
import pygame
import led

from pygame.locals import *



SCALE = 10
SPEED = 20
SIZE = (90, 20)

pygame.init()

fpsClock = pygame.time.Clock()
pixelSurface = pygame.Surface(SIZE)

simDisplay = led.sim.SimDisplay(SIZE)
teensyDisplay = led.teensy.TeensyDisplay() # FIXME this is just a dummy

font = pygame.font.Font("ttf-bitstream-vera-1.10/VeraBd.ttf", 12)

message = font.render("*** Space ist offen & Jens ist nicht kalt !!! ***", True, pygame.Color("#ffffff"))
messageRect = message.get_rect()

x = 10
y = 4
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    x = - ((pygame.time.get_ticks() / SPEED) % (messageRect.width + pixelSurface.get_width()) - pixelSurface.get_width())
    pixelSurface.fill(pygame.Color(0, 0, 0))
    messageRect.topleft = (x, y)
    pixelSurface.blit(message, messageRect)

    fps = font.render("FPS: {:.1f}".format(fpsClock.get_fps()), True, pygame.Color("#ff0000"))
    pixelSurface.blit(fps, (0,0))

    teensyDisplay.update(pixelSurface)
    simDisplay.update(pixelSurface)

    fpsClock.tick(500)