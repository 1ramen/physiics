"""IO for physiics"""
from termcolor import colored

class IO:
    """Static class for handling IO"""
    @staticmethod
    def clear() -> None:
        """Clear the screen"""
        print("\n" * 100)

    @staticmethod
    def cprint(text, color: str) -> None:
        """Print colored text"""
        print(colored(text, color))

    @staticmethod
    def draw(space, verbose=False):
        space = space[::-1]
        print()
        for y in range(len(space)):
            # print the row number
            print(colored("{0: <3}".format(len(space)-y-1),"blue"),end='')
            # loop through and print all of the object in a row
            for x in range(len(space[y])):
                if verbose is True:
                    # print all info on the object
                    print("{}  ".format(space[y][x]),end='')
                else:
                    # print only the object's symbol
                    print("{}  ".format(space[y][x].symbol),end='')
            print()
        # print the column numbers
        print("   ",end='')
        for x in range(len(space[0])):
            print(colored("{0: <2} ".format(x),"blue"),end='')
        print()
        return space