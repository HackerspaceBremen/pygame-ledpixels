import serial
import struct

class PixelDisplay:

    def __init__(self, serialPort, surface):
        self.serial = serial.Serial(serialPort, timeout=1)
        self.serial.write("?")
        config = self.serial.readline().split(",")
        self.width = int(config[0])
        self.height = int(config[1])

        (rM,gM,bM,aM) = surface.get_masks()
        (rS,gS,bS,aS) = surface.get_shifts()
        self.serial.write("+" + struct.pack("IIIBBB", rM, gM, bM, rS, gS, bS))

    def size(self):
        return (self.width, self.height)

    def draw(self, surface):
        buf = surface.get_buffer()
        self.serial.write('*')
        self.serial.write(buf.raw)
