"""Artist puzzles from <http://code.org> built on `tkinter` only. 

Artist is similar to the great `turtle` standard module for teaching
programming but builds on a foundation of puzzle and solution, (which
`turtle` does not):

- Subset of basic Python turtle commands (all needed for puzzles).

- Puzzles created by students with Artist can be checked against
  a known solution saved as JSON.

- New puzzles can be created with Artist by simply `artist.save()` and
  creating challenge stub programs for students to complete that `load()`
  the saved challenge. 

- Artist has only `move_*`, `turn_*`, and `jump_*` and always uses
  verbs to begin method and function names.

- Artist methods correspond one-to-one with those from <http://code.org>
  for easier porting by students.

- Artist supports sprite animation and theming (e.g. zombie, turtle, etc.).

- Artist includes sound and sound theming as well. 

- Artist can be made to be very slow or very, very fast unlike `turtle`

- Artist metaphor matches 'canvas' metaphor used in all graphics coding.

- Artist draws lines individually instead of updating a single line with
  new coordinates so that the artists drawn `lines` can be checked to
  see if the line was drawn forward or backward and give credit for that
  specific line segment. This allows set() to isolate the essential lines
  when checking solutions without throwing out an otherwise good solution
  that was drawn in a different way. This is critical for code.org puzzles
  since often there is more than one way to retrace drawn lines to get
  to a new position.
"""

import os
import json
import math
import random

from .canvas import Canvas
from .gamegrids import XYGrid,xy,slope,bearing,length

class Artist():
    start_direction = 0
    startx = 0
    starty = 0
    color = 'black'
    width = 7
    speed = 'normal'

    def __init__(self,proto=None):
        """In most cases you want Artist.from_json() instead."""
        self.grid = None
        self.solution = None

        # aggregate
        if proto:
            self.canvas = proto.canvas 
            self.puzzle = proto.puzzle
            self.log = proto.log
            self.uid = proto.uid
            self.type = proto.type
            self.x = proto.x
            self.y = proto.y 
            self.direction = proto.start_direction
            self.startx = proto.startx
            self.starty = proto.starty
            self.lastx = proto.lastx
            self.lasty = proto.lasty 
            self.last_direction = proto.direction
        else:
            self.canvas = Canvas()
            self.puzzle = []
            self.log = []
            self.uid = None
            self.type = 'artist'
            self.x = self.startx
            self.y = self.starty 
            self.direction = self.start_direction
            self.lastx = self.x
            self.lasty = self.y 
            self.last_direction = self.direction

        self._lines_to_draw = []          # drawing cache

    @property
    def title(self):
        return self.canvas.title

    @title.setter
    def title(self,new):
        self._title = new
        if not new:
            if self.uid:
                self.canvas.title = self.uid
        else:
            if self.uid:
                self.canvas.title = new + '  [' + self.uid + ']'
            else:
                self.canvas.title = new

    @title.deleter
    def title(self):
        self.canvas.title = self.uid

    def config(self,conf):
        """Sets attributes based dictionary (usually after JSON load)."""
        for key in conf:
            if key in ('startx','starty','start_direction'):
                setattr(__class__,key,conf[key])
            if key in ('puzzle','uid','title','type'):
                setattr(self,key,conf[key])

    def pen_color(self,color):
        """Just to be compatible with 'Show Code' JavaScript"""
        self.color = color

    @classmethod
    def from_json(cls,json_):
        if type(json_) is str:
            json_ = json.loads(json_) 
        instance = cls()
        instance.config(json_)
        return instance

    def setup(self):
        self.title = self._title                     # for missing uid
        self.direction = self.start_direction
        self.x = self.startx
        self.y = self.starty
        self.grid = XYGrid().init(400,400,0)
        self.draw_lines(self.puzzle, color='lightgrey', speed='fastest')
        self.solution = XYGrid(self.grid)
        self.grid = XYGrid().init(400,400,0) # wipe

    def check(self):
        if self.grid == self.solution:
            return self.good_job()
        else:
            if self._close_enough():
                return self.good_job()
            else:
                return self.try_again()

    def _close_enough(self):
        for y in range(400):
            for x in range(400):
                if self.solution[x][y] and not self.grid.ping(x,y):
                    return False
                if self.grid[x][y] and not self.solution.ping(x,y):
                    return False
        return True

    def show_check(self):
        canvas = Canvas()
        for y in range(-200,201):
            for x in range(-200,201):
                if not self.solution[x][y] and not self.grid[x][y]:
                    pass
                elif self.solution[x][y] == self.grid[x][y]:
                    canvas.poke(x,-y,'lightgreen')
                elif self.solution[x][y]:
                    canvas.poke(x,-y,'red')
                elif self.grid[x][y]:
                    canvas.poke(x,-y,'orange')
        self.wait()

    def show_solution(self):
        canvas = Canvas()
        for y in range(-200,201):
            for x in range(-200,201):
                if self.grid[x][y]:
                    canvas.poke(x,-y,'black')
        self.wait()

    def show_lines(self):
        canvas = Canvas()
        for y in range(-200,201):
            for x in range(-200,201):
                if self.grid[x][y]:
                    canvas.poke(x,-y,'black')
        self.wait()

    def show_wrong(self):
        canvas = Canvas()
        for y in range(-200,201):
            for x in range(-200,201):
                if self.grid[x][y] and self.grid[x][y] != self.solution[x][y]:
                    canvas.poke(x,-y,'black')
        self.wait()

    def save(self,name=None,fname=None):
        name = name if name else self.uid
        if os.path.isdir('puzzles'):
            fname = os.path.join('puzzles', name + '.json')
            assert not os.path.isfile(fname), '{} exists'.format(name)
        else:
            fname = name + '.json' 
        with open(fname,'w') as f:
            f.write(json.dumps({
                "uid": self.uid,
                "type": self.type,
                "title": self._title,
                "startx": self.startx,
                "starty": self.starty,
                "start_direction": self.start_direction,
                "puzzle": self.log
            }))

    def try_again(self,message='Nope. Try again.'):
        # TODO replace with a canvas splash window graphic
        print(message)
        self.canvas.exit_on_click()

    def good_job(self,message='Perfect! Congrats!'):
        # TODO replace with a canvas splash window graphic
        print(message)
        self.canvas.exit_on_click()

    def wait_for_click(self):
        return self.good_job('Beautiful!')

    wait = wait_for_click

    def clear(self):
        self._lines_to_draw = []
        self.log = []

    def draw_lines(self,lines,color=None,speed=None):
        self.canvas.speed = speed if speed else self.speed
        self.grid.draw_lines(lines,1)
        if color:
            self.canvas.draw_lines(lines,color=color)
        else:
            self.canvas.draw_lines(lines)
        self.canvas.speed = self.speed

    def _draw(self):
        self.draw_lines(self._lines_to_draw)
        self._lines_to_draw = []

    def _move(self,amount):
        (self.x,self.y) = xy(self.x,self.y,self.direction,amount)

    def move(self,amount):
        self.lastx = self.x
        self.lasty = self.y
        self._move(amount)
        if self.color == 'random':
            color = self.random_color()
        else:
            color = self.color
        line = (self.lastx,self.lasty,self.x,self.y,color,self.width)
        self._lines_to_draw.append(line)
        self.log.append(line)
        self._draw()

    move_forward = move
    forward = move
    fd = move

    def move_backward(self,amount):
        self.move(-amount)

    backward = move_backward
    back = move_backward
    bk = move_backward

    def jump(self,amount):
        self._move(amount)

    jump_forward = jump

    def jump_backward(self,amount):
        self.jump(-amount)

    def turn(self,amount):
        self.last_direction = self.direction
        self.direction += amount
        self.canvas.delay()

    def turn_right(self,amount=90):
        self.turn(amount)

    right = turn_right
    rt = turn_right

    def turn_left(self,amount=90):
        self.turn(-amount)

    left =  turn_left
    lt = turn_left

    def flip(self):
        if self.direction > 0:
            self.direction -= 180
        else:
            self.direction += 180

    rev = flip
    reverse = flip

    @staticmethod
    def random_color():
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        return '#{:02x}{:02x}{:02x}'.format(r,g,b)

    random_colour = random_color
    colour_random = random_color
    color_random = random_color
