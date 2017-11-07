from framework import Behaviour

class Terrified(Behaviour):
    def __init__(self, arbitrator,is_it_close, is_it_scary):
        Behaviour.__init__(arbitrator)
        self.sensobs.append(is_it_close)
        self.sensobs.append(is_it_scary)

    def update(self):
        one,two = self.sense_and_act()
        self.weight = one*two
        return weight,"Scared"

    def sense_and_act(self):
        close = self.sensobs[0].get_value()
        scary = self.sensobs[1].get_value()
        return close,scary
