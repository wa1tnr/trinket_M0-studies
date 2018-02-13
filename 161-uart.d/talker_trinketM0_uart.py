from digitalio import DigitalInOut, Direction
import board
import busio
import time

# uart = busio.UART(board.TX, board.RX, baudrate=9600)
uart = busio.UART(board.D4, board.D3, baudrate=9600)

def emit():
    buf = bytearray(8)    # a buffer to write to the UART
    buf = '+'             # ascii 43 decimal
    uart.write(buf)

while True:
    emit() # talking
    time.sleep(0.025) # limit race condition

