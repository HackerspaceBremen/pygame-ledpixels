import base
import pygame

class SimDisplay(base.Display):
    """ 'Simulation' of the LED display, using pygame.display to show a simulation of the LEDs
    """

    def __init__(self, size, scale = 10):
        super(base.Display, self).__init__()
        self._size = size
        self._scale = scale
        windowSize = tuple([scale * x for x in size])
        self._surface = pygame.display.set_mode(windowSize)

    def size(self):
        return self._size

    def depth(self):
        return self._surface.get_bitsize()

    def update(self, surface):
        pygame.transform.scale(surface, self._surface.get_size(), self._surface)
        pygame.display.update()

