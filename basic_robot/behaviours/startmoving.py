from framework import Behaviour
from motobs.not_scared import NotScared

class StartMoving(Behaviour):

    def __init__(self, am_i_alive):
        super().__init__(NotScared)
        self.sensobs.append(am_i_alive)
        self.stopper = Behaviour()
        self.moving = 0

    def add_stopper(self, behaviour):
        self.stopper = behaviour

    def update(self):
        one = self.sense_and_act()
        if(not self.moving):
            self.weight = one
        else:
            self.weight = 0

    def set_moving(self, number):
        self.moving = number

    def sense_and_act(self):
        value = self.sensobs[0].get_value()
        return value

    def get_weight(self):
        if(self.weight):
            self.moving = 1
            self.weight = 0
            try:
                self.stopper.set_moving(1)
            except:
                pass
            return 1
        return 0