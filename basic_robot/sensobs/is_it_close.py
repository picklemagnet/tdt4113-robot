from framework import Sensob
from utilities.ultrasonic import Ultrasonic
from utilities.irproximity_sensor import IRProximitySensor


class IsItClose(Sensob):
    def __init__(self, sensors):
        super().__init__()
        self.sensors = sensors
        #self.ultra = self.sensors[0]
        #self.ir = self.sensors[1]
        #self.ultra = self.sensors[0]()
        #self.ir = self.sensors[1]()

    def set_priority(self):
        self.update()
        #self.ultra.update()
        value_ultra = self.sensors[0].get_value()

        #self.ir.update()
        value_ir = self.sensors[1].get_value()

        self.value = self._normalize_value(value_ultra, value_ir)

    def _normalize_value(self, ultra, ir):
        ultra = 50 if ultra > 50 else 4 if ultra < 4 else ultra
        ultra = 1 - self._map_range(ultra, 4, 50, 0, 1)
        return max(ultra, *map(float, ir))

    @staticmethod
    def _map_range(oldvalue, oldmin, oldmax, newmin, newmax):
        return (((oldvalue - oldmin) * (newmax - newmin)) / (oldmax - oldmin)) + newmin

