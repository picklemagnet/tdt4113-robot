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


def main():
    bbcon = BBCON(Arbitrator())

    sensobs = [IsItClose, IsItScary, AmIAlive]
    behavs = [CarryOn, FleeBehaviour, StartMoving, StopMoving, Terrified]
    motobs = [HyperScared, NotScared, Scared, Stop]

    for sensob in sensobs:
        bbcon.add_sensob(sensob)
    for behaviour in behavs:
        bbcon.add_behaviour(behaviour)
        bbcon.activate_behaviour(behaviour)
    for motob in motobs:
        bbcon.add_motob(motob)

main()
