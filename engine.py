class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

class Vector:
    def __init__(self, pos=Point(), vel=Point()):
        self.pos = pos
        self.vel = vel

    def __str__(self):
        return "({}+{}, {}+{})".format(x,vx,y,vy)

class Space:
    def __init__(self, dimensions=Point(), friction=1):
        self.width = dimensions.x
        self.height = dimensions.y
        self.friction = friction