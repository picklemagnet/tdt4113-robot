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
        random_step()
