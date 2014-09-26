pygame-ledpixels
================

Displays a pygame Surface on a huge LED display ("LED pixels").

Hardware
--------

The current hardware consists of a matrix of WS2812 LEDs, driven by a Teensy 3.x controller.
The Teensy needs to be running the `TeensyDisplay` sketch contained in this project. Adjust the parameters at the start to match your display configuration.

Installation
------------

`# python setup.py install`

Usage
-----

You can find additional samples in the `samples` folder.

```python
import pygame, led

pygame.init()

# initialize the LED display (serial port will differ on your system)
teensyDisplay = led.teensy.TeensyDisplay("COM3") 

# initialize the simulator display (optional)
simDisplay = led.sim.SimDisplay(teensyDisplay.size())

# create an offscreen surface - this is where the game / graphics will be painted!
pixelSurface = pygame.Surface(teensyDisplay.size())

while True:
  # main loop:
  # - draw your graphics to the offscreen surface
  # - call update() on the display(s)
  
  teensyDisplay.update(pixelSurface)
  simDisplay.update(pixelSurface)

```
