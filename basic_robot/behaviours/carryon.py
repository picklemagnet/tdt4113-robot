from framework import Behaviour
from motobs.not_scared import NotScared

class CarryOn(Behaviour):
    def __init__(self, is_it_close, is_it_scary):
        super().__init__(NotScared)
        self.sensobs.append(is_it_close)
        self.sensobs.append(is_it_scary)

    def update(self):
        one, two = self.sense_and_act()
        self.weight = 0.5 - one*two
        print("carryon weight is " + self.weight)

    def sense_and_act(self):
        close = self.sensobs[0].get_value()
        scary = self.sensobs[1].get_value()
        return close, scary



