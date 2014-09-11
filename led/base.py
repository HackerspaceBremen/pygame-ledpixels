import abc
from abc import ABCMeta, abstractmethod, abstractproperty

class Display:
    """ Base class for displays. Drives the display and provides information about
        the actual hardware.
    """

    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractproperty
    def size(self):
        """
        :return: (tuple) The size of the connected display, in pixels.
        """
        pass

    @abstractproperty
    def depth(self):
        """
        :return: (int) The color depth of the connected display
        """
        pass

    @abstractmethod
    def update(self, surface):
        """
        Update the display using the given pygame.Surface.
        """
        pass