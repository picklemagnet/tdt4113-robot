from framework import Motob, random_step
from utilities.motors import Motors

class Scared(Motob):
    def __init__(self, motors):
        self.motors = motors
        self.value = 0.6

    def update(self):
        self.operationalize()

    #value=(speed[,duration])
    def operationalize(self):
        print("I am scared")
        speed = self.value
        self.motors.backward(speed=speed/2,duration=0.5)
        self.motors.stop()
        self.motors.left(speed=speed,duration=0.25)
        self.motors.forward(speed=speed,duration=0.25)
