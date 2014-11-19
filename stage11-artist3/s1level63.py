"""Stage 11:Puzzle 5 of 11

Draw squares with sides of 50, 60, 70, 80, and 90 pixels. You'll need
to call the `draw_square()` function 5 times.

"""

import sys
sys.path.append('..')
import codestudio
zombie = codestudio.load('s1level63')
zombie.speed = 'fast'

def draw_square(length):
    for count in range(4):
        zombie.move_forward(length)
        zombie.turn_right(90)

draw_square(50)

zombie.check()
