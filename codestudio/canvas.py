"""The Canvas (game board) implemented in tkinter.

While the 'board' metaphor is better for some of the puzzles, 'canvas'
works for the artist and is generally what most graphics frameworks
use when referring to the place where stuff is drawn, whether for games
or art.

Notice that all the details of the graphics framework used to implement
the canvas are hidden away in private methods and attributes. None of
the other classes or functions in the `codestudio` module refer directly
to these implementation details. This allows these canvas classes and
modules to be implemented in any framework without breaking the rest of
the system. This separation of concerns is also the reason our Canvas
class here does not directly subclass the tk.Canvas object.

"""

import tkinter as tk

class Canvas():
    speed_scale = 1000
    speed_slowest = 0.5
    speed_slower = 5 
    speed_slow = 10 
    speed_normal = 40
    speed_fast = 50
    speed_faster = 80
    speed_fastest = 0 
    count = 0

    def __init__(self):
        self.tk = tk.Tk()
        self.tk.geometry('400x400+0+0')
        self.tkcanvas = tk.Canvas(self.tk,
                height=400,width=400, bg='white',
                scrollregion=(-200,-200,200,200))
        self.tkcanvas.pack()
        self._delay = 0 
        self.title = 'codestudio'
        self.speed = 'normal'

    @property
    def title(self):
        return self.tk.title

    @title.setter
    def title(self,value):
        self.tk.title(value)

    @title.deleter
    def title(self):
        self.tk.title('')

    @property
    def speed(self):
        return self.speed

    @speed.setter
    def speed(self,value):
        if isinstance(value,str):
            if   value == 'fastest': value = self.speed_fastest
            elif value == 'faster' : value = self.speed_faster
            elif value == 'fast'   : value = self.speed_fast
            elif value == 'normal' : value = self.speed_normal
            elif value == 'slow'   : value = self.speed_slow
            elif value == 'slower' : value = self.speed_slower
            elif value == 'slowest': value = self.speed_slowest
        if value == 0: 
            self._delay = 0
        else:
            self._delay = round((1/value) * self.speed_scale)

    def exit_on_click(self):
        self.tkcanvas.bind('<Button>',lambda e: self.tk.destroy())
        self.tkcanvas.mainloop()

    def poke(self,x,y,color='black',width=0):
        n = width/2
        self.tkcanvas.create_oval(x-n,y-n,x+n,y+n,fill=color,outline=color)
        self.tkcanvas.update()

    def draw_line(self,line,color=None,width=7):
        n = len(line)
        master_color = color
        if color:
            master_color = color
        coords = (line[0],-line[1],line[2],-line[3])
        if n >= 5:
            color = master_color if master_color else line[4]
        if n >= 6:
            width = line[5]
        self.tkcanvas.create_line(coords, fill=color,
            width=width,capstyle='round',arrow=None)
        self.delay()
        self.tkcanvas.update()

    def delay(self,amount=None):
        amount = amount if amount else self._delay
        if amount != 0:
            self.tkcanvas.after(amount)

    def instance_create(self, cls, x=0, y=0):
        instance  = cls(x,y)
        instance.tk = self.tk
        instance.canvas = self.tkcanvas
        return instance 

class Object():
    """Base Canvas-aware Objects"""

    def __init__(self,x=0,y=0,bearing=0):
        self.tk = None
        self.tkcanvas = None
        self.x = x
        self.y = y
        self.bearing = bearing
        self.sprite = None
        self._visible = True

    @property
    def visible(self):
        return self._visible

    @visible.setter
    def visible(self,value):
        if value == self._visible: 
            return
        if self.sprite:
            self.sprite.visible = value

    @visible.deleter
    def visible(self):
        pass

    def draw(self):
        """Override with instructions for representing object on canvas"""
        if not self._visible:
            return
        # TODO if there is a sprite draw it
        pass

class Sprite():
    def __init__(self,fname=None,imgnum=1,xorig=0,yorig=0,speed=0,angle=0):
        self.fname = fname
        self._image = None
        self._images = []
        self.image = None
        self.imgnum = imgnum
        self.imgindex = 0 
        self.xorig = xorig
        self.yorig = yorig
        self.speed = speed
        self.angle = angle
        self.load(fname)
        self.tkcanvas.create_image(x,y,image=self.sprite)

    def load(self,fname):
        self.image = tk.PhotoImage(file=fname)
        #TODO chop up if _stripXX.gif

