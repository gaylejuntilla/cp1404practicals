import random

from car import Car


class UnreliableCar(Car):
    """UnreliableCar class"""
    def __init__(self, name, fuel, reliability):
        """Initialise Unreliable car object"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive a car if a randomly generated number is greater than the cars reliability"""
        random_number = random.randint(0, 100)
        if random_number < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven
