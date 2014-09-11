import base
import pygame

class TeensyDisplay(base.Display):
    """ A Teensy driven LED display.

        TODO implement this :)
    """

    def __init__(self):
        super(base.Display, self).__init__()
        # TODO implement this

    def size(self):
        # TODO implement this
        pass

    def depth(self):
        # TODO implement this
        pass

    def update(self, surface):
        rgb_pixels = pygame.image.tostring(surface, 'RGB')
        # TODO send RGB pixels