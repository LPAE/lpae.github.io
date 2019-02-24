from random import gauss


class Controller:
    def __init__(self,
                 screen_size,
                 tolerance=1,
                 noise_std_deviation=0.01):

        self.screen_size = screen_size
        self.tolerance = tolerance
        self.noise_std_deviation = noise_std_deviation

    def close_loop_action_control(self, actor, reference, action_power=100):
        for i, actor_pos in enumerate(actor.pos):
            if actor_pos < reference[i] - self.tolerance + self.noise:
                actor.action_force_input[i] += action_power
            elif actor_pos > reference[i] + self.tolerance + self.noise:
                actor.action_force_input[i] -= action_power

    @property
    def noise(self):
        return gauss(mu=0, sigma=self.noise_std_deviation)


