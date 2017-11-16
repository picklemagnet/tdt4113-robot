from framework import Motob, random_step
from motors import Motors

class Scared(Motob):
    def __init__(self):
        motors = Motors()
        self.value = 0

    def update(self,rec):
        self.value = rec
        self.operationalize()

    #value=(speed[,duration])
    def operationalize(self):
        speed,duration = self.value
        motors.backwards(speed=speed//2,duration=duration)
        motors.stop()
        motors.left(speed=speed,duration=0.5)
        motors.forwards(speed=speed,duration=duration)
