import math

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def length(self):
        return math.sqrt(self.x**2, self.y**2)

class Thing(Vector):
    def __init__(self, x=0, y=0, vx=0, vy=0, mass=1, symbol='O')
        # invoke super class
        super(x,y)
        # setup other properties
        self.vx = vx
        self.vy = vy
        self.mass = mass
        self.object = object

    def np(self):
        return Vector(self.x+self.vx, self.y+self.vy)

class Space:
    def __init__(self, width=16, height=16, friction=1, gravity=1):
        # define some basic spacial parameters
        self.width = width
        self.height = height
        self.friction = friction
        self.gravity = gravity
        self.things = []

    def add(self, thing=Thing()):
        self.things += thing

    def update(self):
