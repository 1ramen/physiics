""" Engine for caluculating integer based physics """
from engineio import *
from tools import *
from time import sleep

class Space:
    """Calculate spacial relations"""
    def __init__(self, dimensions: Vector=Vector(16, 16), drag: int=1, gravity: int=1):
        self.dimensions = ~dimensions
        self.drag = Vector(drag)
        self.gravity = gravity
        # populate space with empty objects
        self.space = [[Item() for i in range(self.dimensions.x)] for j in range(self.dimensions.y)]

    def set(self, pos: Vector, item: Item=Item()) -> None:
        """Add a Item to space"""
        print("{} = {}".format(pos, item))
        try:
            self.space[pos.y][pos.x] = item
            return pos
        except:
            return None
        # note: this will overwrite anyItem currently existing at the given location

    def get(self, pos: Vector) -> Item:
        """Get the Item at specified coords"""
        try:
            return self.space[pos.y][pos.x]
        except IndexError:
            # if the specified object is out of bounds return an invalid object ('universal wall')
            return Item(mass=-1)

    def move(self, pos: Vector) -> None:
        """Move Item to new position"""
        # if there is no velocity return
        if self.get(pos).velocity.length() == 0 or self.get(pos).moved is True:
            #IO.cprint("Can't move {} :( [{}]".format(pos, self.get(pos).moved), "red")
            return

        # ensure this item get re-updated
        self.get(pos).moved = True

        # get and clamp the new position
        item = self.get(pos)
        npos = Vector(min(max(self.get(pos).move(pos).x, 0), self.dimensions.x - 1), min(max(self.get(pos).move(pos).y, 0), self.dimensions.y - 1))
        nitem = self.get(npos)

        # if there is nothing the new position, just go there
        if nitem.mass == 0:
            self.set(npos, item)
        else:
            # transfer the velocity to the new item
            self.set(npos, Item(nitem.velocity + item.velocity, nitem.mass, nitem.symbol))
            # move the new item
            self.move(npos)
            # move the old item to the new position and remove it's velocity
            self.set(npos, item)
            self.set(npos, Item(Vector(), item.mass, item.symbol))

        # erase the original position
        self.set(pos)

    def update(self, pos: Vector) -> None:
        """Apply physical forces to an Item"""
        self.get(pos).accelerate(-self.drag)
        self.get(pos).gravity(-self.gravity)

    def update_all(self) -> None:
        """Loop through all of the objects in space and move/update them"""
        # loop through all of the items in space
        for y in range(len(self.space)):
            for x in range(len(self.space[y])):
                # move and update the item
                npos = self.get(Vector(x, y)).move(Vector(x, y))
                self.move(Vector(x, y))
                self.update(npos)

        # clear all 'moved' values to allow action next cycle
        for y in range(len(self.space)):
            for x in range(len(self.space[y])):
                self.get(Vector(x, y)).moved = False

    def prompt(self) -> None:
        """Run interactive prompt for the physics engine"""

        # initialize the commands dict
        commands = {}

        # define I/O versions of all of the methods
        def get_vector(velocity=False) -> Vector:
            if velocity is False:
                return Vector(int(input("X position? ")), int(input("Y position? ")))
            else:
                return Vector(int(input("X velocity? ")), int(input("Y velocity? ")))

        def add() -> None:
            """Add object based on input"""
            # create parameters from user input for new object
            pos = get_vector()
            vel = get_vector(velocity=True)
            mass = int(input("Mass? "))
            try:
                symbol = input("Symbol? ")[0]
            except IndexError:
                symbol = ' '

            # add the generated object to space
            self.set(pos, Item(vel, mass, symbol))

        def remove() -> None:
            """Remove object based on user input"""
            # get location from user
            pos = get_vector()

            # remove object @ given location
            self.set(pos)

        def move() -> None:
            """Wrapper for moving an object"""
            # get location of Item from user
            pos = get_vector()

            # move the Item
            self.move(pos)

        def update() -> None:
            """Wrapper for updating objects"""
            # get location of object to move
            # get location of Item from user
            pos = get_vector()

            # move the Item
            self.update(pos)

        def uall() -> None:
            """Wrapper for updating all of the objects at once"""
            self.update_all()

        def run() -> None:
            """Run the simulation with given parameters"""
            # get the information on the iterations for the simulations
            iterations = int(input("Iterations? "))
            iteration_length = float(input("Iteration length? "))

            # run the simulation
            for i in range(iterations):
                draw()
                uall()
                sleep(iteration_length)

        def draw() -> None:
            """Wrapper for drawing space to the screen with IO class"""
            IO.clear()
            IO.draw(self.space)

        def vdraw() -> None:
            """Draw the space with verbose enabled"""
            IO.draw(self.space, verbose=True)

        def info() -> None:
            """Return info about an object"""
            # get position of item
            pos = get_vector()

            # print the item's info
            IO.cprint(self.get(pos), "blue")

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
            "x":        remove,
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
            "update":   update,
            "u":        update,
            "ua":       uall,
            "~":        uall,
            "run":      run,
            "r":        run,
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
                #IO.clear()
                commands[command]()
            except ValueError:
                # if a command experiences a value error, inform the user that they entered something wrong
                IO.cprint("invalid input", "red")
            except KeyError:
                # if the command given is not found in the dictionary, notify the user
                IO.cprint("unrecognized command", "red")
            except KeyboardInterrupt:
                print()
                continue
        # print out a happy thanks message
        IO.cprint("thanks for using physiics :)", "green")