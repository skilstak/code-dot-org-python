"""Stage 11: Puzzle 2 of 11

Welcome to using functions, which let you define blocks of code! Try the
new `draw_square()` function to draw a small 50x50 green square.

"""

import sys
sys.path.append('..')
import codestudio
zombie = codestudio.load('s1level60')
z = zombie

def draw_square(length):
    for count in range(4):
        zombie.move_forward(length)
        zombie.turn_right(90)

zombie.check()
