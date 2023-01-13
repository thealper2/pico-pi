import utime
from machine import Pin, Timer, ADC

class Pico(object):
    def __init__(self):
        self.led_pin = Pin(25, Pin.OUT)
        self.zamanlayici = Timer()

    def led_toggle(self, zamanlayici):
        self.led_pin.toggle()

    def sicaklik_sensoru_ayarla(self):
        self.sicaklik_sensoru = ADC(4)
    
    def zamanlayici_ayarla(self, frekans, mod, cb):
        self.zamanlayici.init(freq=frekans, mode=mod, callback=cb)
    
    def sicaklik(self):
        fahrenheit = self.sicaklik_sensoru.read_u16() * 3.3 / (65535)
        return 27 - (fahrenheit - 0.706) / (0.001721)

pico = Pico()
pico.zamanlayici_ayarla(2, Timer.PERIODIC, pico.led_toggle)
pico.sicaklik_sensoru_ayarla()

while True:
    sicak = pico.sicaklik()
    print(sicak)
    utime.sleep(2)