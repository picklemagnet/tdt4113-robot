from framework import Behaviour
from motobs.hyperscared import HyperScared

class Terrified(Behaviour):
    def __init__(self, is_it_close, is_it_scary):
        super().__init__(HyperScared)
        self.sensobs.append(is_it_close)
        self.sensobs.append(is_it_scary)

    def update(self):
        one,two = self.sense_and_act()
        self.weight = one*two + 0.1
        if( one < .5 or two < .5):
            self.weight = 0
        return self.weight

    def sense_and_act(self):
        close = self.sensobs[0].get_value()
        scary = self.sensobs[1].get_value()
        return close,scary
