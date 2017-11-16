from framework import Motob,random_step
from motors import Motors

class Stop(Motob):
    def __init__(self):
        self.motors = Motors()
        self.value = 0

    def update(self,rec):
        self.value = rec
        self.operationalize()

    #value=(speed[,duration])
    def operationalize(self):
        self.motors.stop()