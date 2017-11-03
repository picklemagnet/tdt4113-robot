from framework import *
from utilities.ultrasonic import Ultrasonic
from utilities.reflectance_sensors import ReflectanceSensors


class IsItClose(Sensob):
    def __init__(self):
        super().__init__()
        self.sensors = [Ultrasonic(), ReflectanceSensors()]

    def set_value(self):
        ultra, reflectance = self.sensors
        ultra.setup()


isitclose = IsItClose()
isitclose.sensors = [Ultrasonic, ReflectanceSensors]
