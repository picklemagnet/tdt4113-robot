from framework import Motob, random_step
from motors import Motors

class Scared(Motob):
    def __init__(self):
        self.motors = Motors()
        self.value = 0

    def update(self,rec):
        self.value = rec
        self.operationalize()

    #value=(speed[,duration])
    def operationalize(self):
        speed,duration = self.value
        self.motors.backwards(speed=speed//2,duration=duration)
        self.motors.stop()
        self.motors.left(speed=speed,duration=0.5)
        self.motors.forwards(speed=speed,duration=duration)
