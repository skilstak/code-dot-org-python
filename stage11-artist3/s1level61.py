"""Stage 11: Puzzle 3 of 11

Use repeat (for) loops to draw 3 squares of size 100, each 120 degrees
apart. And do it in 3 different, random colors.

Hint: Use your new Zombie class, which we have moved into `mymod.py`
library module for you.

"""

import sys
sys.path.append('..')
import codestudio
zombie = codestudio.load('s1level61')
z = zombie

def draw_square(length):
    for count in range(4):
        zombie.move_forward(length)
        zombie.turn_right(90)

zombie.color = zombie.random_color()
draw_square(100)

zombie.check()
