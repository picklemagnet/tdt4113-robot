from framework import Motob, random_step
from utilities.motors import Motors

class NotScared(Motob):
    def __init__(self, motors):
        self.motors = motors
        self.value = 0

    def update(self):
        self.operationalize()

    #value = (steps[,speed[,duration]])
    def operationalize(self):
        print("I am not scared")
        random_step(self.motors)
