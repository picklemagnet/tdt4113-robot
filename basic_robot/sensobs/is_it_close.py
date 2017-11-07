from framework import Sensob
from utilities.ultrasonic import Ultrasonic
from utilities.reflectance_sensors import ReflectanceSensors


class IsItClose(Sensob):
    def __init__(self):
        super().__init__()
        self.sensors = [Ultrasonic, ReflectanceSensors]
        self.ultra = self.sensors[0]()
        self.reflectance = self.sensors[1]()

    def set_value(self):
        self.ultra.update()
        value_ultra = self.ultra.get_value()

        self.reflectance.update()
        value_reflectance = self.reflectance.get_value()

        print(value_ultra)
        print(value_reflectance)
        print()


isitclose = IsItClose()
isitclose.sensors = [Ultrasonic, ReflectanceSensors]
while True:
    isitclose.set_value()
