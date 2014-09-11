import base
import pygame
import serial

class TeensyDisplay(base.Display):
    """ A Teensy driven LED display.

        TODO implement this :)
    """

    def __init__(self, serialPort):
        super(base.Display, self).__init__()
        self._serial = serial.Serial(serialPort, timeout=1)
        self._query_config()

    def _query_config(self):
        self._serial.write('?')
        _config = self._serial.readline()
        self._size = tuple([int(x) for x in _config.split(',')])

    def size(self):
        return self._size

    def depth(self):
        return 24 # fixed depth

    def update(self, surface):
        rgb_pixels = pygame.image.tostring(surface, 'RGB')
        self._serial.write('*')
        self._serial.write(rgb_pixels)
