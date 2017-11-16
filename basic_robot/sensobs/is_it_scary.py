from framework import Sensob
from PIL import Image
from utilities.imager2 import Imager
from utilities.camera import Camera
import itertools

class IsItScary(Sensob):
    def __init__(self, camera: Camera):
        super().__init__()
        self.sensors.append(camera)

    def average_shade(self, image: Image):
        imager = Imager(image=image)
        colour_sum = 0
        for i in range(imager.xmax):
            for j in range(imager.ymax):
                colour_sum += sum(imager.get_pixel(i,j))/3
        return colour_sum/(imager.xmax*imager.ymax)

    def update(self):
        super().update()
        self.set_value()

    def set_value(self):
        self.value = self.average_shade(self.sensors[0].get_value())/255
