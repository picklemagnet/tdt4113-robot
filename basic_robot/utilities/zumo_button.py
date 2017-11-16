__author__ = 'keithd'
import wiringpi as wp

class ZumoButton():

    def __init__(self):
        wp.wiringPiSetupGpio()  # Dennen linja må ha kjørt hvis motorene skal fungere!!!
        wp.pinMode(22, 0)
        wp.pullUpDnControl(22, 2)
        self.pressed = 0
        self.wait_for_press()

    def wait_for_press(self):
        self.pressed = wp.digitalRead(22)

    def update(self):
        self.wait_for_press()

    def get_value(self):
        return self.pressed

