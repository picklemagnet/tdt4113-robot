from framework import Motob, random_step
from motors import Motors

class Scared(Motob):
    def __init__(self):
        self.motors = Motors()
        self.value = 0.6

    def update(self):
        self.operationalize()

    #value=(speed[,duration])
    def operationalize(self):
        speed = self.value
        self.motors.backwards(speed=speed/2,duration=0.5)
        self.motors.stop()
        self.motors.left(speed=speed,duration=0.25)
        self.motors.forwards(speed=speed,duration=0.25)
