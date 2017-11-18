""" Engine for caluculating integer based physics """

from termcolor import colored
import math

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

class IO:
    """Static class for handling IO"""
    @staticmethod
    def clear():
        """Clear the screen"""
        print("\n" * 100)

    @staticmethod
    def cprint(text, color):
        """Print colored text"""
        print(colored(text, color))

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
        return Vector(0 - self.x, 0 - self.y)

    def __invert__(self):
        return Vector(self.y, self.x)


class Thing:
    """Object in space"""
    def __init__(self, velocity=Vector(), mass=0, symbol='.'):
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
            return
        elif self.velocity.x < 0:
            self.velocity.x = Physics.clamp(self.velocity.x - acceleration.x, maxi=0)
            self.velocity.y = Physics.clamp(self.velocity.y - acceleration.y, maxi=0)
            return

        # return 0 because the value cannot go up or down
        return 0

    def update(self, drag=0, friction=Vector(), gravity=0):
        """Update the object's velocity based on environment values"""
        # increase friction with air drag
        friction += Vector(drag)

        # apply gravity and friction
        self.velocity.y -= int(gravity)
        self.acc(-friction)

class Space:
    """Calculate spacial relations"""
    def __init__(self, dimensions=Vector(), friction=1, drag=1, gravity=1):
        self.dimensions = dimensions
        self.friction = friction
        self.drag = drag
        self.gravity = gravity
        self.space = [[Thing() for i in range(self.dimensions.y)] for j in range(self.dimensions.x)]

    def add(self, thing=Thing(), pos=Vector()):
        """Add a Thing to space"""
        self.space[pos.x][pos.y] = thing
        return pos
        # note: this will overwrite anything currently existing at the given location

    def remove(self, pos=Vector()):
        """Remove anything at a given position"""
        self.space[pos.x][pos.y] = Thing()
        return pos

    def prompt(self):
        """Run interactive prompt for the physics engine"""

        # define I/O versions of all of the methods
        def add():
            """Add object based on input"""
            try:
                # create parameters from user input for new object
                pos = Vector(int(input("X position? ")), int(input("Y position? ")))
                vel = Vector(int(input("X velocity? ")), int(input("Y velocity? ")))
                mass = int(input("Mass? "))
                symbol = input()[0]
            except ValueError:
                IO.cprint("invalid input", "red")
                return None

            # add the generated object to space
            return self.add(Thing(vel, mass, symbol), pos)

        def remove():
            """Remove object based on user input"""
            # get location from user
            pos = Vector(int(input("X position? ")), int(input("Y position? ")))

            # remove object @ given location
            return self.remove(pos)

        def quit():
            """Placeholder function so no error is returned when quit is entered"""
            return None

        # define all of the commands
        commands = {
            "q":      quit,
            "quit":   quit,
            "exit":   quit,
            "add":    add,
            "a":      add,
            "new":    add,
            "n":      add,
            "remove": remove,
            "rem":    remove,
            "clear":  remove,
            "delete": remove,
            "del":    remove,
            "d":      remove,
        }
        command = ""

        # loop and check for commands
        while command not in ["quit", "q", "exit"]:
            command = input("> ")
            # execute the specified command
            try:
                IO.clear()
                commands[command]()
            except KeyError:
                IO.clear()
                IO.cprint("unrecognized command", "red")
        IO.cprint("thanks for using physiics :)", "green")