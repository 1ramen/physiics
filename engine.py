import math
from time import sleep

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def length(self):
        return math.sqrt(self.x**2, self.y**2)

class Thing:
    def __init__(self, vel=Vector(), pos=Vector(), mass=0, symbol='.'):
        # setup other properties
        self.vel = vel
        self.pos = pos
        self.mass = mass
        self.object = object
        self.symbol = symbol

    def __str__(self):
        return "[({},{})({},{}),{},{}]".format(self.pos.x,self.pos.y,self.vel.x,self.vel.y,self.mass,self.symbol)

    def move(self):
        return Vector(self.pos.x+self.vel.x, self.pos.y+self.vel.y)

class Space:
