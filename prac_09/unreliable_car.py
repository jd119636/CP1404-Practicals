import random

from prac_09.car import Car


class UnreliableCar(Car):
    """Subclass of car which is Unreliable."""
    def __init__(self, name: str, fuel: float, reliability: float):
        super().__init__(name, fuel)
        self.name = name
        self.fuel = fuel
        self.reliability = reliability

    def drive(self, distance):
        """generates a random number between 0 and 100 every time you want to drive and if its lower
         than the reliability it will drive the car."""
        random_number = random.uniform(0, 100)

        if random_number < self.reliability:
            # Drive normally (use the parent method)
            return super().drive(distance)
        else:
            # Drive fails — no distance travelled
            return 0
