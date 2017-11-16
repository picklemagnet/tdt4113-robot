from framework import Motob, random_step
from utilities.motors import Motors

class NotScared(Motob):
    def __init__(self):
        self.value = 0
        self.motors = Motors()

    def update(self):
        self.operationalize()

    #value = (steps[,speed[,duration]])
    def operationalize(self):
        random_step(self.motors)
