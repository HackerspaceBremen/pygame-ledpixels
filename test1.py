import sys
import pygame
import pixelDisplay

from pygame.locals import *


SCALE = 10
SPEED = 20

pygame.init()
pygame.display.set_mode()

pixelDisplay = pixelDisplay.PixelDisplay("/dev/cu.usbmodem458221")
pixelSize = pixelDisplay.get_size()

fpsClock = pygame.time.Clock()

windowSize = tuple([SCALE * x for x in pixelSize])
windowSurface = pygame.display.set_mode(windowSize)

pixelSurface = pixelDisplay.get_surface()

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

    x = - ((pygame.time.get_ticks() / SPEED) % (messageRect.width + pixelDisplay.width) - pixelDisplay.width)
    pixelSurface.fill(pygame.Color(0, 0, 0))
    messageRect.topleft = (x, y)
    pixelSurface.blit(message, messageRect)

    pixelDisplay.draw()
    pygame.transform.scale(pixelSurface, windowSize, windowSurface)
    fps = font.render("FPS: {:.1f}".format(fpsClock.get_fps()), True, pygame.Color("#ff0000"))
    windowSurface.blit(fps, (5, 5))
    pygame.display.update()

    fpsClock.tick(30)