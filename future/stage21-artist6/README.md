Stage 21 - Artist 6
===================

Stage 21? Yeah, there isn't one on code.org, but if there were it would
likely be about Object Oriented Programming. OOP is the natural next
step having learned about variables, functions and the rest. In fact,
without it the puzzles involving functions up to now look slightly odd,
and for good reason.  The `draw_snowman()` function is really best as
a method that belongs to a Zombie class. Notice the puzzle solution:

```
import sys
sys.path.append('..')
import codestudio
zombie = codestudio.load('s1level67')

def draw_snowman(length):
    zombie.left()
    distances = [length * 0.5, length * 0.3, length * 0.2]
    for counter in range(6):
        distance = distances[counter if counter < 3 else 5 - counter] / 57.5
        for degree in range(90):
            zombie.move(distance)
            zombie.right(2)
        if counter != 2:
            zombie.left(180)
    zombie.left()

zombie.speed = 'fastest'

for count in range(3):
    zombie.color = zombie.random_color()
    draw_snowman(150)                            # ??? no zombie?
    zombie.right()
    zombie.jump(100)
    zombie.left()

zombie.check()
```
As a 

Why not import \*?
==================

Because it is almost never the right thing to do and teaching it to
those just starting out is a bad idea. The pernicious `from turtle
import *` and `from tkinter import *` are some of the biggest flaws of
all Python beginner education. Calling `forward()` as an implied method
of a base class violates 'explicit over implicit' rule championed by
great programmers of all languages. Why foist this bad habit on those
who don't know better?

Instead start beginners out right by training them to always associate
a method explicitly with its object, `muddy.forward()` for example.
