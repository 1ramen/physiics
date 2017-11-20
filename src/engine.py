""" Engine for caluculating integer based physics """
from engineio import *
from tools import *

class Space:
    """Calculate spacial relations"""
    def __init__(self, dimensions=Vector(16, 16), drag=1, gravity=1):
        self.dimensions = ~dimensions
        self.drag = drag
        self.gravity = gravity
        # populate space with empty objects
        self.space = [[Thing() for i in range(self.dimensions.y)] for j in range(self.dimensions.x)]

    def set(self, pos=Vector(), thing=Thing()):
        """Add a Thing to space"""
        self.space[pos.x][pos.y] = thing
        return pos
        # note: this will overwrite anything currently existing at the given location

    def get(self, x, y):
        try:
            return self.space[x][y]
        except IndexError:
        # if the specified
            return Thing(mass=-1)

    def prompt(self):
        """Run interactive prompt for the physics engine"""

        # initialize the commands dict
        commands = {}

        # define I/O versions of all of the methods
        def add():
            """Add object based on input"""
            try:
                # create parameters from user input for new object
                pos = Vector(int(input("X position? ")), int(input("Y position? ")))
                vel = Vector(int(input("X velocity? ")), int(input("Y velocity? ")))
                mass = int(input("Mass? "))
                symbol = input("Symbol? ")[0]
            # if the user inputs something wrong inform them and quit
            except ValueError:
                IO.cprint("invalid input", "red")
                return None

            # add the generated object to space
            return self.set(pos, Thing(vel, mass, symbol))

        def remove():
            """Remove object based on user input"""
            try:
                # get location from user
                pos = Vector(int(input("X position? ")), int(input("Y position? ")))
            except ValueError:
                # if the user inputs something wrong inform them
                IO.cprint("invalid input", "red")
                return None

            # remove object @ given location
            return self.set(pos)

        def draw():
            """Wrapper for drawing space to the screen with IO class"""
            return IO.draw(self.space)

        def vdraw():
            """Draw the space with verbose enabled"""
            return IO.draw(self.space, verbose=True)

        def move():
            """Move an object"""
            try:
                return self.move(Vector(int(input("X position? ")), int(input("Y position? "))))
            except ValueError:
                # if the user inputs something wrong inform them
                IO.cprint("invalid input", "red")
                return None

        def info():
            """Return info about an object"""
            try:
                IO.clear()
                return print(IO.cprint(self.space[int(input("X position? "))][int(input("Y position? "))], "blue"))
            except ValueError:
                # if the user inputs something wrong inform them
                IO.cprint("invalid input", "red")
                return None

        def ehelp():
            """Print out the commands"""
            for item in commands:
                print(item)

            return len(commands)

        def quit():
            """Placeholder function so no error is returned when quit is entered"""
            return None

        def update():
            return self.update()

        # define all of the commands
        commands = {
            "q":        quit,
            "quit":     quit,
            "exit":     quit,
            "add":      add,
            "a":        add,
            "new":      add,
            "n":        add,
            "remove":   remove,
            "rm":       remove,
            "clear":    IO.clear,
            "delete":   remove,
            "del":      remove,
            "draw":     draw,
            "d":        draw,
            "vdraw":    vdraw,
            "v":        vdraw,
            "move":     move,
            "mv":       move,
            "info":     info,
            "i":        info,
            "inf":      info,
            "help":     ehelp,
            "halp":     ehelp,
            "h":        ehelp,
            "cmds":     ehelp,
            "commands": ehelp,
            "update":   update,
            "u":        update,

        }
        command = ""

        # loop and check for commands
        IO.clear()
        while command not in ["quit", "q", "exit"]:
            # get a command from the user
            command = input("> ")
            try:
                # execute the specified command
                IO.clear()
                commands[command]()
            except KeyError:
                # if the command given is not found in the dictionary, notify the user
                IO.clear()
                IO.cprint("unrecognized command", "red")
        # print out a happy thanks message
        IO.cprint("thanks for using physiics :)", "green")