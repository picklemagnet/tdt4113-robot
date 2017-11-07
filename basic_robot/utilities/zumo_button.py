__author__ = 'keithd'
import wiringpi2 as wp

class ZumoButton():

    def __init__(self):
        wp.wiringPiSetupGpio()  # Dennen linja må ha kjørt hvis motorene skal fungere!!!
        wp.pinMode(22, 0)
        wp.pullUpDnControl(22, 2)
        self.pressed = 0
        self.wait_for_press()

    def wait_for_press(self):
        read_val = wp.digitalRead(22)
        while read_val:
            read_val = wp.digitalRead(22)
        self.pressed = 1 - self.pressed

    def update(self):
        self.wait_for_press()

    def get_value(self):
        return self.pressed

