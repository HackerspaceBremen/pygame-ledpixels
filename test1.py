import sys
import pygame
import pixelDisplay

from pygame.locals import *


SCALE = 10
SPEED = 20

pixelDisplay = pixelDisplay.PixelDisplay("/dev/cu.usbmodem458221")
pixelSize = pixelDisplay.size()

pygame.init()
fpsClock = pygame.time.Clock()

windowSize = tuple([SCALE * x for x in pixelSize])
windowSurface = pygame.display.set_mode(windowSize)

pixelSurface = pygame.Surface(pixelSize)

font = pygame.font.Font("ttf-bitstream-vera-1.10/VeraBd.ttf", 12)

message = font.render("*** HSHB *** Hello World ***", True, pygame.Color("#ffffff"))
messageRect = message.get_rect()

x = 10
y = 4
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    x = - ((pygame.time.get_ticks() / SPEED) % (messageRect.width + pixelDisplay.width) - pixelDisplay.width)
    pixelSurface.fill(pygame.Color(0, 0, 0))
    messageRect.topleft = (x, y)
    pixelSurface.blit(message, messageRect)

    pixelDisplay.draw(pixelSurface)
    pygame.transform.scale(pixelSurface, windowSize, windowSurface)
    fps = font.render("FPS: {:.1f}".format(fpsClock.get_fps()), True, pygame.Color("#ff0000"))
    windowSurface.blit(fps, (5, 5))
    pygame.display.update()

    fpsClock.tick(30)