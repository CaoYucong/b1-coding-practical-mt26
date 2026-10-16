class PDController:
    # Initialise the PD gains and controller state.
    def __init__(self):
        self.kp = 0.15
        self.kd = 0.6
        self.previous_error = 0.0

    # Reset the previous error before starting a new simulation.
    def reset(self):
        self.previous_error = 0.0

    # Calculate the control action from the reference and observed depth.
    def __call__(self, reference, observation):
        error = reference - observation

        # Apply the specified PD control law.
        action = self.kp * error + self.kd * (error - self.previous_error)

        # Store the current error for the next simulation step.
        self.previous_error = error

        return action