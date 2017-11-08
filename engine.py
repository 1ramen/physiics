import math

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def length(self):
        return math.sqrt(self.x**2, self.y**2)

class Thing:
    def __init__(self, vel=Vector(), pos=Vector(), mass=0, symbol='.')
        # setup other properties
        self.vel = vel
        self.pos = pos
        self.mass = mass
        self.object = object

    def velocity(self):
        return self.vel

class Space:
    def __init__(self, width=16, height=16, friction=1, gravity=1):
        # define some basic spatial parameters
        self.width = width
        self.height = height
        self.friction = friction
        self.gravity = gravity
        self.space = [[Thing() for x in range(self.width)] for y in range(self.height)]

    def add(self, thing=Thing()):
        """Write object to given location"""
        self.space[thing.pos.x][thing.pos.y] = thing

    def remove(self, x, y):
        """Remove thing at given location"""
        self.space[x][y] = Thing()

    def clamp(self, mx, c):
        """Make sure given value is within reasonable bounds"""
        if c > mx:
            return mx
        elif c < 0:
            return 0
        else:
            return c

    def update(self):
        # loop through all of the objects in space
        for x in range(len(space)):
            for y in range(len(space[x])):
                # save the object at this location
                thing = space[x][y]
                # write an empty object to the empty space
                space[x][y] = Thing()
                # update the object's coords
                thing.pos.x = clamp(width, thing.vel.x+x)
                thing.pos.y = clamp(height, thing.vel.y+y)
                # write the new coords to the space
                space[thing.x][thing.y] = thing
                # update the velocity
                thing.vel.x -= self.friction
                thing.vel.y -= self.gravity

    def draw(self):
        for x in range(len(space)):
            for y in range(len(space[x])):
                print(space[x][y].symbol)
            print("\n")

space = Space()
