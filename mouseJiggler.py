import time
import usb_hid
import board
import digitalio
from adafruit_hid.mouse import Mouse

mouse = Mouse(usb_hid.devices)
led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT

led.value = False
time.sleep(10)
while True:
    led.value = True
    mouse.move(x=10)
    led.value = False
    time.sleep(1)
    
    led.value = True
    mouse.move(x=-10)
    led.value = False
    time.sleep(1)