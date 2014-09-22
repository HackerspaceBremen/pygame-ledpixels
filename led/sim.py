import base
import pygame

GRIDCOLOR = pygame.Color(20,20,20)

class SimDisplay(base.Display):
    """ 'Simulation' of the LED display, using pygame.display to show a simulation of the LEDs
    """

    def __init__(self, size, scale = 10):
        super(base.Display, self).__init__()
        self._size = size
        self._scale = scale
        windowSize = tuple([scale * x for x in size])
        try:
            self._surface = pygame.display.set_mode(windowSize)
        except pygame.error as e:
            # fallback
            print "Display error:" , e.message
            print "SIM display will not work."
            self._surface = None

    def size(self):
        return self._size

    def depth(self):
        if self._surface:
            return self._surface.get_bitsize()
        else: return 0

    def draw_grid(self, surface):
        x0 = y0 = 0
        x1 = surface.get_width()
        y1 = surface.get_height()

        while x0 <= surface.get_width():
            pygame.draw.line(surface, GRIDCOLOR, (x0, 0), (x0, y1))
            x0 += self._scale

        while y0 <= surface.get_height():
            pygame.draw.line(surface, GRIDCOLOR, (0, y0), (x1, y0))
            y0 += self._scale

    def update(self, surface):
        if self._surface:
            pygame.transform.scale(surface, self._surface.get_size(), self._surface)
            self.draw_grid(self._surface)
            pygame.display.update()

