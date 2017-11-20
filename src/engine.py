""" Engine for caluculating integer based physics """
from engineio import *
from tools import *

class Space:
    """Calculate spacial relations"""
    def __init__(self, dimensions: Vector=Vector(16, 16), drag: int=1, gravity: int=1):
        self.dimensions = ~dimensions
        self.drag = drag
        self.gravity = gravity
        # populate space with empty objects
        self.space = [[Item() for i in range(self.dimensions.x)] for j in range(self.dimensions.y)]

    def set(self, pos: Vector, item: Item=Item()) -> None:
        """Add a Item to space"""
        print("{} := {}".format(pos, item))
        self.space[pos.y][pos.x] = item
        # note: this will overwrite anyItem currently existing at the given location

    def get(self, pos: Vector) -> Item:
        """Get the Item at specified coords"""
        try:
            return self.space[pos.y][pos.x]
        except IndexError:
        # if the specified
            return Item(mass=-1)

    def move(self, pos: Vector) -> None:
        """Move Item to new position"""
        # if there is no velocity return
        if self.get(pos).velocity.length() == 0:
            return
        # copy current Item to the new location
        self.set(self.get(pos).move(pos), self.get(pos))
        # erase original Item
        self.set(pos)

    def update(self, pos: Vector):
        """Apply physical forces to an Item"""
        self.get(pos).accelerate(self.drag)
        self.get(pos).gravity(self.gravity)

    def update_all(self) -> None:
        """Loop through all of the objects in space and move/update them"""

    def prompt(self) -> None:
        """Run interactive prompt for the physics engine"""

        # initialize the commands dict
        commands = {}

        # define I/O versions of all of the methods
        def add() -> None:
            """Add object based on input"""
            try:
                # create parameters from user input for new object
                pos = Vector(int(input("X position? ")), int(input("Y position? ")))
                vel = Vector(int(input("X velocity? ")), int(input("Y velocity? ")))
                mass = int(input("Mass? "))
                symbol = input("Symbol? ")[0]
            # if the user inputs someItem wrong inform them and quit
            except ValueError:
                IO.cprint("invalid input", "red")
                return

            # add the generated object to space
            self.set(pos, Item(vel, mass, symbol))

        def remove() -> None:
            """Remove object based on user input"""
            try:
                # get location from user
                pos = Vector(int(input("X position? ")), int(input("Y position? ")))
            except ValueError:
                # if the user inputs something wrong inform them
                IO.cprint("invalid input", "red")
                return

            # remove object @ given location
            self.set(pos)

        def move() -> None:
            """Wrapper for moving an object"""
            try:
                # get location of Item from user
                pos = Vector(int(input("X position? ")), int(input("Y position? ")))
            except ValueError:
                # if the user inputs something wrong inform them
                IO.cprint("invalid input", "red")
                return

            # move the Item
            self.move(pos)

        def draw() -> None:
            """Wrapper for drawing space to the screen with IO class"""
            IO.draw(self.space)

        def vdraw() -> None:
            """Draw the space with verbose enabled"""
            IO.draw(self.space, verbose=True)

        def info() -> None:
            """Return info about an object"""
            try:
                IO.clear()
                # get information on an item and print it
                pos = Vector(int(input("X position? ")), int(input("Y position? ")))
                IO.cprint(self.get(pos), "")
            except ValueError:
                # if the user inputs something wrong inform them
                IO.cprint("invalid input", "red")
            except IndexError:
                # if the user's inputted item location has no item, inform them
                IO.cprint("specified item doesn't exist", "red")

        def ehelp() -> None:
            """Print out the commands"""
            for item in commands:
                print(item)

        def quit() -> None:
            """Placeholder function so no error is returned when quit is entered"""
            return

        # define all of the commands
        commands = {
            "q":        quit,
            "quit":     quit,
            "exit":     quit,
            "add":      add,
            "a":        add,
            "new":      add,
            "n":        add,
            "+":        add,
            "remove":   remove,
            "rem":      remove,
            "r":        remove,
            "-":        remove,
            "clear":    IO.clear,
            "c":        IO.clear,
            "delete":   remove,
            "del":      remove,
            "draw":     draw,
            "d":        draw,
            "vdraw":    vdraw,
            "v":        vdraw,
            "info":     info,
            "i":        info,
            "inf":      info,
            "help":     ehelp,
            "halp":     ehelp,
            "h":        ehelp,
            "?":        ehelp,
            "cmds":     ehelp,
            "commands": ehelp,
            "move":     move,
            "m":        move,
        }
        command = ""

        # loop and check for commands
        IO.clear()
        while command not in ["quit", "q", "exit"]:
            # get a command from the user
            try:
                command = input("> ")
            except KeyboardInterrupt:
                return
            try:
                # execute the specified command
                IO.clear()
                commands[command]()
            except KeyError:
                # if the command given is not found in the dictionary, notify the user
                IO.clear()
                IO.cprint("unrecognized command", "red")
            except KeyboardInterrupt:
                IO.clear()
        # print out a happy thanks message
        IO.cprint("thanks for using physiics :)", "green")