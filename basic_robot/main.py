from framework import *
from sensobs.is_it_close import IsItClose
from sensobs.is_it_scary import IsItScary
from sensobs.amialive import AmIAlive
from behaviours.carryon import CarryOn
from behaviours.flee import FleeBehaviour
from behaviours.startmoving import StartMoving
from behaviours.stopmoving import StopMoving
from behaviours.terrified import Terrified
from motobs.hyperscared import HyperScared
from motobs.not_scared import NotScared
from motobs.scared import Scared
from motobs.stop import Stop
from utilities.camera import Camera
from utilities.irproximity_sensor import IRProximitySensor
from utilities.ultrasonic import Ultrasonic
from utilities.zumo_button import ZumoButton

def main():
    print("hello again mr freeman")
    bbcon = BBCON(Arbitrator())

    sensobs = [IsItClose([Ultrasonic(), IRProximitySensor()]), IsItScary(Camera()), AmIAlive(ZumoButton())]
    behavs = [CarryOn(sensobs[0], sensobs[1]),
              FleeBehaviour(sensobs[0], sensobs[1]),
              StartMoving(sensobs[2]),
              Terrified(sensobs[0], sensobs[1])]

    behavs.append(StopMoving(behavs[2], sensobs[2]))
    motobs = [HyperScared, NotScared, Scared, Stop]

    for sensob in sensobs:
        bbcon.add_sensob(sensob)
    for behaviour in behavs:
        bbcon.add_behaviour(behaviour)
        bbcon.activate_behaviour(behaviour)
    for motob in motobs:
        bbcon.add_motob(motob)

    while True:
        bbcon.run_one_timestep()


print("hello")
main()
