from framework import Motob, random_step

class NotScared(Motob):
    def __init__(self):
        self.value = 0

    def update(self,rec):
        self.value = rec
        self.operationalize()

    #value = (steps[,speed[,duration]])
    def operationalize(self):
        random_step()
