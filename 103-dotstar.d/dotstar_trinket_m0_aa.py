# Trinket IO demo
# Welcome to CircuitPython 2.0.0 :)

import board
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogOut, AnalogIn
import touchio
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import adafruit_dotstar as dotstar
import time
import neopixel

# One pixel connected internally!
dot = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.2)

# Built in red LED
led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

# Analog input on D0
analog1in = AnalogIn(board.D0)

# Analog output on D1
aout = AnalogOut(board.D1)

# Digital input with pullup on D2
button = DigitalInOut(board.D2)
button.direction = Direction.INPUT
button.pull = Pull.UP

# Capacitive touch on D3
touch = touchio.TouchIn(board.D3)

# NeoPixel strip (of 16 LEDs) connected on D4
NUMPIXELS = 16
neopixels = neopixel.NeoPixel(board.D4, NUMPIXELS, brightness=0.2, auto_write=False)

# Used if we do HID output, see below
kbd = Keyboard()

######################### HELPERS ##############################

# Helper to convert analog input to voltage
def getVoltage(pin):
    return (pin.value * 3.3) / 65536

# Helper to give us a nice color swirl
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if (pos < 0):
        return [0, 0, 0]
    if (pos > 255):
        return [0, 0, 0]
    if (pos < 85):
        return [int(pos * 3), int(255 - (pos*3)), 0]
    elif (pos < 170):
        pos -= 85
        return [int(255 - pos*3), 0, int(pos*3)]
    else:
        pos -= 170
        return [0, int(pos*3), int(255 - pos*3)]

######################### MAIN LOOP ##############################


def startup():
    i = 0
    while True:
        dot[0] = wheel(i & 255)
        for p in range(NUMPIXELS):
            idx = int ((p * 256 / NUMPIXELS) + i)
            neopixels[p] = wheel(idx & 255)
        neopixels.show()
        aout.value = i * 256
        if touch.value:
            print("D3 touched!")
        led.value = touch.value
        if not button.value:
            print("Button on D2 pressed!")
        i = (i+1) % 256  # run from 0 to 255
        time.sleep(0.11)

