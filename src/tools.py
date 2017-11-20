"""Basic tools for building the engine"""

import math
from engineio import *

class Physics:
    """Static class with methods for easier computation"""
    @staticmethod
    def clamp(value, mini=None, maxi=None):
        """Clamp a value into a given range"""
        # ensure that all values are defined
        if mini is None:
            mini = value
        if max is None:
            maxi = value

        # clamp n based on min and max
        if int(value) < int(mini):
            return int(mini)
        elif int(value) > int(maxi):
            return int(maxi)
        return int(value)

class Vector:
    """XY pair for calculating motion"""
    def __init__(self, x=0, y=None):
        if y is None:
            y = x
        self.x = int(x)
        self.y = int(y)

    def length(self):
        """Return vector length"""
        # use pythagorean theorem to calculate the overall length
        return math.sqrt(self.x ** 2, self.y ** 2)

    def reset(self):
        """Clear the Vector"""
        # set the vector to a default value and return it
        self = Vector()
        return self

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        return Vector(self.x / other.x, self.y / other.y)

    def __floordiv__(self, other):
        return Vector(self.x // other.x, self.y // other.y)

    def __iadd__(self, other):
        self = self + other

    def __isub__(self, other):
        self = self - other

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __invert__(self):
        return Vector(self.y, self.x)


class Thing:
    """Object in space"""
    def __init__(self, velocity=Vector(), mass=0, symbol=' '):
        self.velocity = velocity
        self.mass = mass
        self.symbol = symbol

    def __str__(self):
        return "<{}, {}, '{}'>".format(self.velocity.__str__(), self.mass, self.symbol)

    def acc(self, acceleration=Vector()):
        """Accelerate the object by a given ammount"""
        # if there is no second term assume that the first applies to both
        if acceleration.y is None:
            acceleration.y = acceleration.x

        # pull value to zero
        if self.velocity.x > 0:
            self.velocity.x = Physics.clamp(self.velocity.x + acceleration.x, mini=0)
            self.velocity.y = Physics.clamp(self.velocity.y + acceleration.y, mini=0)
            return self.velocity
        elif self.velocity.x < 0:
            self.velocity.x = Physics.clamp(self.velocity.x - acceleration.x, maxi=0)
            self.velocity.y = Physics.clamp(self.velocity.y - acceleration.y, maxi=0)
            return self.velocity

        # return 0 because the value cannot go up or down
        return 0