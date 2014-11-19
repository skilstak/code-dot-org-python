"""Stage 11: Puzzle 2 of 11

Welcome to using object-oriented programming! Classes, objects, methods
and attributes! We'll use our zombie artist but with more power!  Still no
reason fear. For this puzzle complete the method in the Zombie class so
your zombie will draw a small 50x50 green square.

Classes are used to make objects (like classification, not school
class). Sometimes we use the word 'instance' instead of 'object'. You
have been using objects all along. An `artist` is an object instance
of the `Artist` class. Note the capital letter 'A'. Class names are
always capitalized.

Methods are special functions tied to a class. They tell us what objects
from that class can do. For example, all artists can `move_forward(100)`.
Methods always have a dot linking them to the object from that class
(`artist.move_forward(100)`). Methods usually start with a verb, but
not always.

Attributes are special variables tied to a class. They tell us about the
object and let us change them. For example, all artists have 'color',
'width', and 'speed' attributes that we have been changing. Usually
we change attributes like any variable, by assigning to them
(`artist.color = 'red'`). Sometimes attributes are changed with methods
(`artist.pencolor('red')`). It really just depends on how the class
was designed.

Classes really help us out because they let us organize code into objects
like in the real-world so thinking about them makes sense when your
code gets long and complicated (as most all code does). This is called
"object-oriented programming". We think you'll love it. Let's build a
Zombie class using OOP!

"""

import sys
sys.path.append('..')
import codestudio

class Zombie(codestudio.Artist):
    """An Artist who likes to eat brains and draw squares.

    Class definitions look like function definitions but are
    different. The parameter inside the parenthesis (`codestudio.Artist`)
    says that Zombies can do everything an Artist can do.

    The `start_direction` and `speed` are special variables that goes
    with all Zombies. These are called class or static attributes. An
    attribute is a variable that goes with a class or the objects created
    from a class.

    """

    start_direction = 90            # facing the east, or right of screen
    speed = 'slow'                  # it is a zombie after all
    color = 'green'                 # it is a zombie after all

    def draw_square(self,length):
        pass                                     # ???

#----------------------------------------------------------------
"""
We still need an artist so we can let the zombie use his puzzle and
canvas to draw on. We won't see the artist though. He took a break
and and let's the zombie do all the work.
"""

artist = codestudio.load('s1level60')
zombie = Zombie(artist)
zombie.draw_square(50)

zombie.check()
