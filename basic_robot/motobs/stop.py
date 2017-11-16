from framework import Motob,random_step
from utilities.motors import Motors

class Stop(Motob):
    def __init__(self):
        self.motors = Motors()
        self.value = 0

    def update(self):
        self.operationalize()

    #value=(speed[,duration])
    def operationalize(self):
        self.motors.stop()