from framework import Sensob


class AmIAlive(Sensob):
    def __init__(self, zumo_button):
        super().__init__()
        self.sensors.append(zumo_button)

    def set_value(self):
        self.value = self.sensors[0].get_value()

    def get_value(self):
        return self.value
