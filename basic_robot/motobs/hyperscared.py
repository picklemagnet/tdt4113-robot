from framework import Motob,random_step
from utilities.motors import Motors

class HyperScared(Motob):
    def __init__(self):
        self.motors = Motors()
        self.value = 0

    def update(self):
        self.operationalize()

    #value=(speed[,duration])
    def operationalize(self):
        speed = self.value
        self.stop()
        self.motors.left(speed=speed,duration=0.25)
        self.motors.right(speed=speed,duration=0.75)
