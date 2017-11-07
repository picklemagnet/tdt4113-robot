from framework import Motob,random_step
from motors import Motors

class NotScared(Motob):
    def __init__(self):
        self.value = 0

    def update(self,rec):
        self.value = rec
        self.operationalize()

    #value = (steps[,speed[,duration]])
    def operationalize(self):
        for i in range(value[0]):
            if len(value)==1:
                random_step(m,speed=speed,duration=0.5)
            elif len(value)==2:
                random_step(m,speed=value[1],duration=0.5)
            elif len(value)==3:
                random_step(m,speed=value[1],duration=value[2])
