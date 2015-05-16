import sys
import socket
import select
import base
import pygame
import base64

class DisplayServerClientDisplay(base.Display):
    """ A Display Server client display, see

            https://github.com/HackerspaceBremen/pixels_displayserver

        for the display server code.
        This connects to the display server and sends data via a socket.
    """

    def __init__(self, host, port, fallbackSize = (60, 40)):
        super(base.Display, self).__init__()
        self._buf = ""
        self._size = fallbackSize

        try:
            self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._connect(host, port)
            self._query_config()
        except Exception as e:
            # fallback
            print "Display error:" , e.message
            print "LED display will not work, using fallback size {0}".format(fallbackSize)
            self._socket = None

    def _connect(self, host, port):
        self._socket.connect((host, port))
        # expect: connect: ok
        value = self._readproperty('connect')
        print "Connect response: " + value

        # expect: session-id: <id>
        value = self._readproperty('session-id')
        print "Session ID: " + value

    def _query_config(self):
        self._socket.sendall('info: ?\n\n')
        value = self._readproperty('info-geometry');
        print "Display Geometry: " + value
        self._size = tuple([int(x) for x in value.split(',')])

    def _readproperty(self, property):
        prop, value = None, None
        while prop != property:
            prop, value = self._readline()

        return value.strip()

    def _readline(self, bufsize=4096):
        if self._socket:
            while True:
                if self._buf.find('\n') != -1:
                    line, self._buf = self._buf.split('\n', 1)
                    print "Recv Line: " + repr(line)

                    if line.strip() != '':
                        return line.split(':', 1)
                    else:
                        return ('', '')

                self._buf += self._socket.recv(bufsize)

    def size(self):
        return self._size

    def depth(self):
        return 24 # fixed depth

    def update(self, surface):
        if self._socket:
            readable, writable, exceptional = select.select([self._socket], [], [], 0)

            if readable:
        		self._buf += self._socket.recv(4096)
        		
            rgb_pixels = pygame.image.tostring(surface, 'RGB')
            #self._serial.write('*')
            #self._serial.write(rgb_pixels)
            base64_pixels = base64.b64encode(rgb_pixels)
            self._socket.sendall("blit: 0,0,{0},{1}\n".format(self._size[0], self._size[1]))
            self._socket.sendall("data: " + base64_pixels + "\n\n")

            status = self._readproperty('blit')
            print "Blit status: " + status
