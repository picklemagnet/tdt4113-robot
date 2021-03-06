from framework import Behaviour
from motobs.stop import Stop

class StopMoving(Behaviour):

    def __init__(self, start_moving, am_i_alive):
        super().__init__(Stop)

        self.checker = start_moving
        self.moving = 0
        self.sensobs.append(am_i_alive)

    def update(self):
        one = self.sense_and_act()
        if self.moving:
            self.weight = one


    def sense_and_act(self):
        value = self.sensobs[0].get_value()
        return value

    def set_moving(self, number):
        self.moving = number

    def get_weight(self):
        if self.weight:
            self.moving = 0
            self.weight = 0
            try:
                self.checker.set_moving(0)
            except:
                pass
            return 1
        return 0