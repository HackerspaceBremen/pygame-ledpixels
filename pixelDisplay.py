import serial
import pygame

class PixelDisplay:

    def __init__(self, serialPort):
        self.serial = serial.Serial(serialPort)
        self.serial.write("?")
        config = self.serial.readline().split(",")
        self.width = int(config[0])
        self.height = int(config[1])

        self.framedata = bytearray(3 + (self.width * self.height * 3))

    def size(self):
        return (self.width, self.height)

    def draw(self, surface):
        pxArray = pygame.PixelArray(surface)
        self.framedata[0] = '$'
        self.framedata[1] = 0
        self.framedata[2] = 0

        written = self.serial.write(self.framedata)
        if (written != len(self.framedata)):
            raise Exception('error writing frame data')

        millis = int(self.serial.readline())
        print(millis)
        del pxArray