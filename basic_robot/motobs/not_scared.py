from framework import Motob, random_step
from utilities.motors import Motors
from random import randint

class NotScared(Motob):
    def __init__(self, motors):
        self.motors = motors
        self.value = 0.3

    def update(self):
        self.operationalize()

    #value = (steps[,speed[,duration]])
    def operationalize(self):
        print("I am not scared")
        speed = self.value
        i = randint(1, 3)   
        if(i == 1):
            self.motors.left(speed=speed, dur = 0.25)
            self.motors.forward(speed=speed, dur = 0.75)
        elif(i == 2):
            self.motors.right(speed=speed, dur=0.25)
            self.motors.forward(speed=speed, dur=0.75)
        elif(i == 3):
            self.motors.right(speed=speed, dur=0.5)
            self.motors.left(speed=speed, dur=0.5)
        else:
            self.motors.left(speed=speed, dur=0.25)
            self.motors.right(speed=speed, dur=0.25)
            self.motors.left(speed=speed, dur=0.25)
            self.motors.right(speed=speed, dur=0.25)

