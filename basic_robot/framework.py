class Arbitrator:
    def __init__(self):
        self.behaviours = []
        self.active_behaviours = []
        self.sensobs = []
        self.motobs = []
        self.arbitrator = []

    def add_behaviour(self, behaviour):
        self.behaviours.append(behaviour)

    def add_sensob(self, sensob):
        self.sensobs.append(sensob)

    def activate_behaviour(self, behaviour):
        self.active_behaviours.append(behaviour)

    def deactivate_behaviour(self, behaviour):
        self.behaviours.remove(behaviour)

    def run_one_timestep(self):
        pass

    def choose_action(actions,self):
        # Return tuple containing motor recommendations (one per motob) and a boolean indicating
        # whether or not the run should be halted
        return max(actions)[1]


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


class Behaviour:
    def __init__(self, arbitrator):
        self.arbitrator = arbitrator
        self.sensobs = []
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



