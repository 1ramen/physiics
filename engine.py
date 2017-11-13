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
    def __init__(self, vel=Vector(), pos=Vector(), mass=0, symbol='.'):
        # setup other properties
        self.vel = vel
        self.pos = pos
        self.mass = mass
        self.object = object
        self.symbol = symbol

    def __str__(self):
        return "[({},{})({},{}),{},{}]".format(self.pos.x, self.pos.y, self.vel.x, self.vel.y, self.mass, self.symbol)

    def velocity(self):
        return self.vel

class Space:
    def __init__(self, width=16, height=8, friction=1, gravity=1):
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
        """Update all of the objects in space"""
        # loop through all of the objects in space
        for x in range(len(self.space)):
            for y in range(len(self.space[x])):
                # save the object at this location
                thing = self.space[x][y]
                # write an empty object to the empty space
                self.space[x][y] = Thing()
                # update the object's coords
                thing.pos.x = self.clamp(self.width, thing.vel.x+thing.pos.x)
                thing.pos.y = self.clamp(self.height, thing.vel.y+thing.pos.y)
                # write the new coords to the space
                self.space[thing.pos.x][thing.pos.y] = thing
                # update the velocity
                thing.vel.x -= self.friction
                thing.vel.y -= self.gravity

    def draw(self):
        """Draw space"""
        for x in range(len(self.space)):
            for y in range(len(self.space[x])):
                print(self.space[x][y].symbol,end='')
            print("\n")

    def vdraw(self):
        """Draw space with all information of the blocks"""
        for x in range(len(self.space)):
            for y in range(len(self.space[x])):
                print(self.space[x][y],end='')
            print("\n")

    def prompt(self):
        """Setup interactive prompt for manipulating physical space"""
        cmd = ""
        while cmd != "quit":
            cmd = input(">")
            if cmd == "draw":
                print("\n" * 100)
                self.draw()
            elif cmd == "update":
                self.update()
            elif cmd == "add":
                self.add(Thing(Vector(int(input("X Position? ")), int(input("Y Position? "))), Vector(int(input("X Velocity? ")), int(input("Y Velocity? "))), int(input("Mass? ")), input("Symbol? ")[0]))
            elif cmd == "remove":
                self.remove(input("X Position? "), input("Y Position? "))
            elif cmd == "obj":
                self.vdraw()
            else:
                print("unrecognized command")
        print("\n" * 100)

space = Space()
space.prompt()
