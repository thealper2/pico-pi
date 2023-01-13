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
mouse.move(y=450)
click = 1

while True:
    while click > 0:
        led.value = TRUE
        mouse.click(Mouse.LEFT_BUTTON)
        time.sleep(0.1)
        click = click - 1
    led.value = False
    time.sleep(30)