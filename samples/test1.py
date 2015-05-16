import sys
import pygame
import led

from pygame.locals import *

speed = 30

pygame.init()
pygame.display.set_mode()

fpsClock = pygame.time.Clock()

#teensyDisplay = led.teensy.TeensyDisplay(sys.argv[1])
dsDisplay = led.dsclient.DisplayServerClientDisplay('localhost', 8123)
simDisplay = led.sim.SimDisplay(dsDisplay.size())
pixelSurface = pygame.Surface(dsDisplay.size())

font = pygame.font.SysFont("Arial", 12)

message = font.render("*** This is a test message *** ", True, pygame.Color("#00ff00"))
messageRect = message.get_rect()

x = 10
y = 4
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    x = - ((pygame.time.get_ticks() / speed) % (messageRect.width + pixelSurface.get_width()) - pixelSurface.get_width())
    pixelSurface.fill(pygame.Color(0, 0, 0))
    messageRect.topleft = (x, y)
    pixelSurface.blit(message, messageRect)

    fps = font.render("FPS: {:.1f}".format(fpsClock.get_fps()), True, pygame.Color("#ff0000"))
    #pixelSurface.blit(fps, (0,0))

    dsDisplay.update(pixelSurface)
    simDisplay.update(pixelSurface)

    fpsClock.tick(30)
