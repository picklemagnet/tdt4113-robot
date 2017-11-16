from random import choice, randint


def random_step(motors,speed=0.25,duration=1):
    dir = choice(['forward', 'backward', 'left', 'right'])
    eval('Motors.' + dir)(motors, speed, duration)


class BBCON:
    def __init__(self, arbitrator):
        self.behaviours = []
        self.active_behaviours = []
        self.sensobs = []
        self.motobs = []
        self.arbitrator = arbitrator

    def add_behaviour(self, behaviour):
        self.behaviours.append(behaviour)

    def add_sensob(self, sensob):
        self.sensobs.append(sensob)

    def activate_behaviour(self, behaviour):
        self.active_behaviours.append(behaviour)

    def deactivate_behaviour(self, behaviour):
        self.active_behaviours.remove(behaviour)

    def run_one_timestep(self):
        for sensob in self.sensobs:
            sensob.update()
        for behaviour in self.behaviours:
            behaviour.update()
        actions = [(x.weight, x.motob) for x in self.active_behaviours]
        motob = self.arbitrator.choose_action(actions)
        motob.update()


class Sensob:
    def __init__(self):
        self.sensors = []
        self.value = 0

    def update(self):
        for sensor in self.sensors:
            sensor.update()

    def set_value(self):
        pass
        # DO STUFF HERE with sensor.get_value()


class Arbitrator:
    def __init__(self):
        pass

    def choose_action(self, actions, deterministic=True):
        if deterministic:
            return max(actions)[1]
        else:
            s = sum(zip(*actions).__next__())
            weighted = [x[0] for x in actions]
            rand_act = randint(0, 100)
            for i in range(len(weighted)):
                weighted[i] = 100 * weighted[i] / s
                if i > 0:
                    weighted[i] += weighted[i-1]
                if weighted[i] >= rand_act:
                    return actions[i][1]
        # Return tuple containing motor recommendations (one per motob) and a boolean indicating
        # whether or not the run should be halted


class Behaviour:
    def __init__(self, motob):
        self.sensobs = []
        self.motob = motob
        self.weight = 0  # priority * match_degree

    def sense_and_act(self):
        pass  # Read data from sensobs, and set match_degree and motor_recommendations

    def update(self):
        pass  # Call sense_and_act, and update weight


class Motob:
    def __init__(self):
        self.motors = []
        self.value = 0

    def update(self):
        pass

    def operationalize(self):
        pass

