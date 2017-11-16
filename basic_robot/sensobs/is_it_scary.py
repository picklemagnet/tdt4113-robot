from framework import Sensob
from PIL import Image
from utilities.imager2 import Imager
from utilities.camera import Camera
import itertools

class IsItScary(Sensob):
    def __init__(self, camera: Camera):
        super().__init__()
        self.sensors.append(camera)
        #self.counter = 0

    def average_shade(self, image: Image):
        imager = Imager(image=image)
        colour_sum = 0
        for i in range(imager.xmax):
            for j in range(imager.ymax):
                colour_sum += sum(imager.get_pixel(i, j))/3
        return colour_sum/(imager.xmax*imager.ymax)

    def update(self):
        #if(not(self.counter)):
        super().update()
        self.set_value()
        #self.counter = (self.counter + 1) % 4

    def set_value(self):
        value = self.average_shade(self.sensors[0].get_value())/255
        value = 0.37 if value > 0.37 else value
        value = 1 - self._map_range(value, 0, 0.37, 0, 1)
        self.value = value

    @staticmethod
    def _map_range(oldvalue, oldmin, oldmax, newmin, newmax):
        return (((oldvalue - oldmin) * (newmax - newmin)) / (oldmax - oldmin)) + newmin
