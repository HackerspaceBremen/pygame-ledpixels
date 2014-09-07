import serial
import pygame
import array

class PixelDisplay:

    def __init__(self, serialPort):
        self.serial = serial.Serial(serialPort, timeout=1)
        self.serial.write("?")
        config = self.serial.readline().split(",")
        self.width = int(config[0])
        self.height = int(config[1])

        self.framedata = bytearray(3 + (self.width * self.height * 3))

    def size(self):
        return (self.width, self.height)

    def map_color(self, c):
        return (c.g << 16) | (c.r << 8) | (c.b) # GRB

    def draw(self, surface):
        pxArray = pygame.PixelArray(surface)
        self.framedata[0] = '$'
        self.framedata[1] = 0
        self.framedata[2] = 0

        (width, height) = pxArray.shape

        linesPerPin = self.height / 8
        offset = 3
        pixels = array.array('I', range(8))

        for y in range(linesPerPin):
            if y & 1 == 0:
                xbegin = 0
                xend = width
                xinc = 1
            else:
                xbegin = width - 1
                xend = -1
                xinc = -1

            for x in range(xbegin, xend, xinc):
                for i in range(8):
                    color = pxArray[x, y + linesPerPin * i]
                    pixels[i] = self.map_color(surface.unmap_rgb(color))

                mask = 0x800000
                while mask != 0:
                    b = 0
                    for i in range(8):
                        if (pixels[i] & mask) != 0:
                            b |= (1 << i)
                    self.framedata[offset] = b
                    offset += 1
                    mask >>= 1

        written = self.serial.write(self.framedata)
        del pxArray