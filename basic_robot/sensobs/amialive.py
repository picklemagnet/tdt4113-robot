from framework import Sensob


class AmIAlive(Sensob):
    def __init__(self, Zumo_Button):
        Sensob.__init__()
        self.sensobs.append(Zumo_Button)


    def set_value(self):
        self.value = self.sensobs[0].get_value()

    def get_value(self):
        return self.value
