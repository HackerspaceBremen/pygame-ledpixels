import sys
import pygame
import pygame.freetype
import pixelDisplay

from pygame.locals import *


SCALE = 10
SPEED = 30

pixelDisplay = pixelDisplay.PixelDisplay("COM3")
pixelSize = pixelDisplay.size()

pygame.init()
fpsClock = pygame.time.Clock()

windowSize = tuple([SCALE * x for x in pixelSize])
windowSurface = pygame.display.set_mode(windowSize)

pixelSurface = pygame.Surface(pixelSize)

font = pygame.freetype.Font("ttf-bitstream-vera-1.10/VeraMono.ttf", size = 12)

(message, messageRect) = font.render("Hello World", fgcolor = pygame.Color("#ffffff"))

x = 10
y = (pixelSurface.get_height() / 2) - (message.get_height() / 2)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    x = - ((pygame.time.get_ticks() / SPEED) % (messageRect.width + pixelDisplay.width) - pixelDisplay.width)
    pixelSurface.fill(pygame.Color("#000000"), messageRect)
    messageRect.topleft = (x, y)
    pixelSurface.blit(message, messageRect)

    pixelDisplay.draw(pixelSurface)
    pygame.transform.scale(pixelSurface, windowSize, windowSurface)
    font.render_to(windowSurface, (5,5), "FPS: {:.1f}".format(fpsClock.get_fps()), fgcolor = pygame.Color("#ff0000"))
    pygame.display.update()

    fpsClock.tick(30)