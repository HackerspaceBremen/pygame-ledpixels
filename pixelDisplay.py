import pygame
import serial
import struct

class PixelDisplay:

    def __init__(self, serialPort):
        pygame.init()

        self.serial = serial.Serial(serialPort, timeout=1)
        self.serial.write("?")
        config = self.serial.readline().split(",")
        self.width = int(config[0])
        self.height = int(config[1])
        self.surface = pygame.Surface(self.get_size())
        (rM,gM,bM,aM) = self.surface.get_masks()
        (rS,gS,bS,aS) = self.surface.get_shifts()
        self.serial.write("+" + struct.pack("IIIBBB", rM, gM, bM, rS, gS, bS))

    def get_surface(self):
        return self.surface

    def get_size(self):
        return (self.width, self.height)

    def draw(self):
        buf = self.surface.get_buffer()
        self.serial.write('*')
        self.serial.write(buf.raw)
