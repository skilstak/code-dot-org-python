from collections import UserList
import math

class XYGrid(UserList):
    """Traditional coordinate game grid.

    grid = XYGrid().init(10,10,'~')
    grid[1][2] = '*'
    print(grid)

    """

    def __init__(self,value=[[]]):
        self.data = value

    def init(self,xsize=0,ysize=0,value=None):
        self.xsize = xsize
        self.ysize = ysize
        self.data = [[value for y in range(ysize+1)] for x in range(xsize+1)]
        for x in range(xsize+1):
            self.data[x][0] = ''
        for y in range(ysize+1):
            self.data[0][y] = ''
        return self

    def to_text(self):
        d = self.data
        string = ''
        for y in range(self.ysize):
            for x in range(self.xsize):
                string += str(d[x+1][y+1]) + ' '
            string += "\n"
        return string

    def ping(self,x,y):

        try: hx = self.data[x+1]
        except: hx = False

        try: mx = self.data[x]
        except: mx = False

        try: lx = self.data[x-1]
        except: lx = False

        try: hxhy = hx[y+1]
        except: hxhy = False

        try: hxmy = hx[y]
        except: hxmy = False

        try: hxly = hx[y-1]
        except: hxly = False

        try: mxhy = mx[y+1]
        except: mxhy = False

        try: mxmy = mx[y]
        except: mxmy = False

        try: mxly = mx[y-1]
        except: mxly = False

        try: lxhy = lx[y+1]
        except: lxhy = False

        try: lxmy = lx[y]
        except: lxmy = False

        try: lxly = lx[y-1]
        except: lxly = False
        if hxhy or hxmy or hxly or mxhy or mxmy or mxly or lxhy or lxmy or lxly:
            return True
        return False

    def draw_line(self,line,value=1):
        (x1,y1,x2,y2) = [round(n) for n in line[0:4]]
        m = slope((x1,y1,x2,y2))
        if m is None:                           # vertical line
            if y1 <= y2:
                for y in range(y1,y2+1):
                    self.data[x1][y] = value
            else:
                for y in range(y1,y2-1,-1):
                    self.data[x1][y] = value
        else:
            b = y1 - (m*x1)
            if x1 <= x2:
                for x in range(x1,x2+1):
                    y = round(m*x+b)
                    self.data[x][y] = value
            else:
                for x in range(x1,x2-1,-1):
                    y = round(m*x+b)
                    self.data[x][y] = value

    def draw_lines(self,lines,value=None):
        for line in lines:
            self.draw_line(line,value)

    def points_with(self,value):
        points = []
        for x in range(len(self.data)):
            for y in range(len(self.data[x])):
                if self.data[x][y] == value:
                    points.append((x,y))
        return set(points)

def bearing(line):
    angle = math.degrees(math.atan2(line[3]-line[1],line[2]-line[0]))
    if 0 <= angle <= 90:
        return 90 - angle
    elif 90 < angle <= 180:
        return 180 - angle + 270 
    elif 0 > angle >= -90:
        return 90 - angle
    elif -90 > angle >= -180:
        return 90 - angle

def slope(line):
    x1 = line[0]
    y1 = line[1]
    x2 = line[2]
    y2 = line[3]
    dx = x2 - x1
    dy = y2 - y1
    if not dx:
        return None
    else:
        return dy / dx

def length(line):
    """Thank you Pythagoras. You would have loved Python."""
    return math.sqrt((line[2] - line[0]) ** 2 + (line[3] - line[1]) ** 2)

def xy(x=0, y=0, direction=0.0, amount=0):
    """Returns a new (x,y) coordinate after adding the amount in
    the given direction."""
    angle = math.radians(float(direction))
    return (math.sin(angle) * amount + x, math.cos(angle) * amount + y)

class XYZGrid(UserList):
    """Adds 3rd dimension mostly for layering on XYGrids"""
    pass

class XYBitGrid(UserList):
    """Ultra fast XY grid as packed struct composed of boolean on/offs"""
    pass
