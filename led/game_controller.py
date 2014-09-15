import serial

BTN_P1_BLUE    =34
BTN_P1_RED     =32
BTN_P1_YELLOW  =30
BTN_P1_UP      =28
BTN_P1_DOWN    =24
BTN_P1_LEFT    =26
BTN_P1_RIGHT   =22

BTN_P2_BLUE    =40
BTN_P2_RED     =38
BTN_P2_YELLOW  =36
BTN_P2_UP      =48
BTN_P2_DOWN    =44
BTN_P2_LEFT    =46
BTN_P2_RIGHT   =42

class GameController:
    def __init__(self, serialPort):
        try:
            self._serial = serial.Serial(serialPort, 115200, timeout=0)
        except Exception as e:
            # fallback
            print "Game controller error:" , e.message
            print "Game controller will not work"
            self._serial = None

    def get_events(self):
        _events = []
        _event = bytearray(1)
        while self._serial.readinto(_event) > 0:
            _events.append((int(_event[0]) & 0xFE, int(_event[0]) & 0x01))

        return _events