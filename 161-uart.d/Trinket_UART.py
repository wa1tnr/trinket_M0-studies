# Trinket IO demo - USB/Serial echo

# [ https://learn.adafruit.com/adafruit-trinket-m0-circuitpython-arduino/circuitpython-uart-serial ]

from digitalio import DigitalInOut, Direction
import board
import busio
import time

led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

# You can also use board.TX and board.RX for prettier code!
#                               D4 and D3 are the TX/RX pair on the trinket M0?
uart = busio.UART(board.D4, board.D3, baudrate=9600)


while True:
    data = uart.read(32)  # read up to 32 bytes
    #print(data)          # this is a bytearray type

    if data != None:
        led.value = True

	# datastr = ''.join([chr(b) for b in data]) # convert bytearray to string
        datastr = str(data, 'ascii')
	print(datastr, end="")

        led.value = False

# Dan Halbert:

# str(thebytearray, 'ascii')
