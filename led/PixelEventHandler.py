__author__ = 'Jannes Hoeke'

from pygame.locals import *

# Return values
UP, DOWN, LEFT, RIGHT, B1, B2, B3, P1, P2, UNKNOWN = range(10)
PUSH, RELEASE = range(2)
PLAYER1, PLAYER2 = range(2)

# Player 1 Keyboard bindings (defaults)
KB_UP_1 = K_UP
KB_DOWN_1 = K_DOWN
KB_LEFT_1 = K_LEFT
KB_RIGHT_1 = K_RIGHT
KB_B1_1 = K_COMMA
KB_B2_1 = K_PERIOD
KB_B3_1 = K_MINUS

# Player 2 Keyboard bindings (defaults)
KB_UP_2 = K_w
KB_DOWN_2 = K_s
KB_LEFT_2 = K_a
KB_RIGHT_2 = K_d
KB_B1_2 = K_c
KB_B2_2 = K_v
KB_B3_2 = K_b

# Neutral bindings
KB_P1 = K_1
KB_P2 = K_2

class PixelEvent:
    def __init__(self, button, type, player):
        self.button = button
        self.type = type
        self.player = player

_last_ax0 = None
_last_ax1 = None
_last_ax2 = None
_last_ax3 = None

# event should be of type pygame.event.Event
def process_event(event):
    global _last_ax0, _last_ax1, _last_ax2, _last_ax3

    try:
        # Keypresses on keyboard and joystick axis motions / button presses
        if event.type == KEYDOWN or event.type == JOYAXISMOTION and event.value != 0 or event.type == JOYBUTTONDOWN:
            # Directional - Player 1
            if event.type == KEYDOWN and event.key == KB_UP_1 or event.type == JOYAXISMOTION and event.axis == 1 and event.value < 0:
                _last_ax1 = UP
                return PixelEvent(UP, PUSH, PLAYER1)
            elif event.type == KEYDOWN and event.key == KB_DOWN_1 or event.type == JOYAXISMOTION and event.axis == 1 and event.value > 0:
                _last_ax1 = DOWN
                return PixelEvent(DOWN, PUSH, PLAYER1)
            elif event.type == KEYDOWN and event.key == KB_RIGHT_1 or event.type == JOYAXISMOTION and event.axis == 0 and event.value > 0:
                _last_ax0 = RIGHT
                return PixelEvent(RIGHT, PUSH, PLAYER1)
            elif event.type == KEYDOWN and event.key == KB_LEFT_1 or event.type == JOYAXISMOTION and event.axis == 0 and event.value < 0:
                _last_ax0 = LEFT
                return PixelEvent(LEFT, PUSH, PLAYER1)

            # Directional - Player 2
            elif event.type == KEYDOWN and event.key == KB_UP_2 or event.type == JOYAXISMOTION and event.axis == 3 and event.value < 0:
                _last_ax3 = UP
                return PixelEvent(UP, PUSH, PLAYER2)
            elif event.type == KEYDOWN and event.key == KB_DOWN_2 or event.type == JOYAXISMOTION and event.axis == 3 and event.value > 0:
                _last_ax3 = DOWN
                return PixelEvent(DOWN, PUSH, PLAYER2)
            elif event.type == KEYDOWN and event.key == KB_RIGHT_2 or event.type == JOYAXISMOTION and event.axis == 2 and event.value > 0:
                _last_ax2 = RIGHT
                return PixelEvent(RIGHT, PUSH, PLAYER2)
            elif event.type == KEYDOWN and event.key == KB_LEFT_2 or event.type == JOYAXISMOTION and event.axis == 2 and event.value < 0:
                _last_ax2 = LEFT
                return PixelEvent(LEFT, PUSH, PLAYER2)

            # Buttons
            elif event.type == KEYDOWN and event.key == KB_B1_1 or event.type == JOYBUTTONDOWN and event.button == 1:
                return PixelEvent(B1, PUSH, PLAYER1)
            elif event.type == KEYDOWN and event.key == KB_B2_1 or event.type == JOYBUTTONDOWN and event.button == 2:
                return PixelEvent(B2, PUSH, PLAYER1)
            elif event.type == KEYDOWN and event.key == KB_B3_1 or event.type == JOYBUTTONDOWN and event.button == 3:
                return PixelEvent(B3, PUSH, PLAYER1)
            elif event.type == KEYDOWN and event.key == KB_B1_2 or event.type == JOYBUTTONDOWN and event.button == 4:
                return PixelEvent(B1, PUSH, PLAYER2)
            elif event.type == KEYDOWN and event.key == KB_B2_2 or event.type == JOYBUTTONDOWN and event.button == 5:
                return PixelEvent(B2, PUSH, PLAYER2)
            elif event.type == KEYDOWN and event.key == KB_B3_2 or event.type == JOYBUTTONDOWN and event.button == 6:
                return PixelEvent(B3, PUSH, PLAYER2)

            # Playerbuttons
            elif event.type == KEYDOWN and event.key == KB_P1 or event.type == JOYBUTTONDOWN and event.button == 7:
                return PixelEvent(P1, PUSH, PLAYER1)
            elif event.type == KEYDOWN and event.key == KB_P2 or event.type == JOYBUTTONDOWN and event.button == 8:
                return PixelEvent(P2, PUSH, PLAYER2)

        # Button/Key releases or joystick home position
        elif event.type == KEYUP or event.type == JOYAXISMOTION and event.value == 0.0 or event.type == JOYBUTTONUP:
            # Directional - Player 1
            if event.type == KEYUP and event.key == KB_UP_1 or event.type == JOYAXISMOTION and event.axis == 1 and _last_ax1 == UP:
                return PixelEvent(UP, RELEASE, PLAYER1)
            elif event.type == KEYUP and event.key == KB_DOWN_1 or event.type == JOYAXISMOTION and event.axis == 1 and _last_ax1 == DOWN:
                return PixelEvent(DOWN, RELEASE, PLAYER1)
            elif event.type == KEYUP and event.key == KB_RIGHT_1 or event.type == JOYAXISMOTION and event.axis == 0 and _last_ax0 == RIGHT:
                return PixelEvent(RIGHT, RELEASE, PLAYER1)
            elif event.type == KEYUP and event.key == KB_LEFT_1 or event.type == JOYAXISMOTION and event.axis == 0 and _last_ax0 == LEFT:
                return PixelEvent(LEFT, RELEASE, PLAYER1)

            # Directional - Player 2
            elif event.type == KEYUP and event.key == KB_UP_2 or event.type == JOYAXISMOTION and event.axis == 3 and _last_ax3 == UP:
                return PixelEvent(UP, RELEASE, PLAYER2)
            elif event.type == KEYUP and event.key == KB_DOWN_2 or event.type == JOYAXISMOTION and event.axis == 3 and _last_ax3 == DOWN:
                return PixelEvent(DOWN, RELEASE, PLAYER2)
            elif event.type == KEYUP and event.key == KB_RIGHT_2 or event.type == JOYAXISMOTION and event.axis == 2 and _last_ax2 == RIGHT:
                return PixelEvent(RIGHT, RELEASE, PLAYER2)
            elif event.type == KEYUP and event.key == KB_LEFT_2 or event.type == JOYAXISMOTION and event.axis == 2 and _last_ax2 == LEFT:
                return PixelEvent(LEFT, RELEASE, PLAYER2)

            # Buttons
            elif event.type == KEYUP and event.key == KB_B1_1 or event.type == JOYBUTTONUP and event.button == 1:
                return PixelEvent(B1, RELEASE, PLAYER1)
            elif event.type == KEYUP and event.key == KB_B2_1 or event.type == JOYBUTTONUP and event.button == 2:
                return PixelEvent(B2, RELEASE, PLAYER1)
            elif event.type == KEYUP and event.key == KB_B3_1 or event.type == JOYBUTTONUP and event.button == 3:
                return PixelEvent(B3, RELEASE, PLAYER1)
            elif event.type == KEYUP and event.key == KB_B1_2 or event.type == JOYBUTTONUP and event.button == 4:
                return PixelEvent(B1, RELEASE, PLAYER2)
            elif event.type == KEYUP and event.key == KB_B2_2 or event.type == JOYBUTTONUP and event.button == 5:
                return PixelEvent(B2, RELEASE, PLAYER2)
            elif event.type == KEYUP and event.key == KB_B3_2 or event.type == JOYBUTTONUP and event.button == 6:
                return PixelEvent(B3, RELEASE, PLAYER2)

            # Playerbuttons
            elif event.type == KEYUP and event.key == KB_P1 or event.type == JOYBUTTONUP and event.button == 7:
                return PixelEvent(P1, RELEASE, PLAYER1)
            elif event.type == KEYUP and event.key == KB_P2 or event.type == JOYBUTTONUP and event.button == 8:
                return PixelEvent(P2, RELEASE, PLAYER2)

        return PixelEvent(UNKNOWN, -1, -1)
    # We tried to process an event that we should not have processed
    except AttributeError:
        print("AttributeError on " + str(event))
        return PixelEvent(UNKNOWN, -1, -1)

