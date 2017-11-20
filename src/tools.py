"""Basic tools for building the engine"""

import math
from engineio import *

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
        return math.sqrt(self.x ** 2 + self.y ** 2)

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


class Item:
    """Object in space"""
    def __init__(self, velocity=Vector(), mass=0, symbol=' '):
        self.velocity = velocity
        self.mass = mass
        self.symbol = symbol

    def __str__(self):
        return "<{}, {}, '{}'>".format(self.velocity.__str__(), self.mass, self.symbol)

    def accelerate(self, acceleration: Vector) -> Vector:
        """Accelerate the object by a given ammount"""
        # if there is no second term assume that the first applies to both
        if acceleration.y is None:
            acceleration.y = acceleration.x

        # update the velocity ensuring that if it is decelerating, it doesn't go below zero
        if self.velocity.x > 0:
            self.velocity.x = max(self.velocity.x + acceleration.x, 0)
        elif self.velocity.x < 0:
            self.velocity.x = min(self.velocity.x - acceleration.x, 0)

        if self.velocity.y > 0:
            self.velocity.y = max(self.velocity.y + acceleration.y, 0)
        elif self.velocity.x > 0:
            self.velocity.y = min(self.velocity.y - acceleration.y, 0)

        # return the updated velocity
        return self.velocity

    def gravity(self, gravity: int) -> None:
        """Apply given gravitaional constant to Item"""
        self.velocity.y -= gravity

    def move(self, pos: Vector) -> Vector:
        """Calculate the new position of a point using the given Item's velocity"""
        print("MOVE: {} + {} = {}".format(pos, self.velocity, pos + self.velocity))
        return pos + self.velocity