"""Stage 15: Puzzle 8 of 10

Here is all of the code from the previous puzzle. Modify `draw_house()`
so I end up at the bottom right corner after drawing a new house. Use
this modified function to draw three houses.

"""

import sys
sys.path.append('..')
import codestudio
z = codestudio.load('s1level89')

def draw_square(length):
    for count in range(4):
        z.move_forward(length)
        z.turn_right(90)

def draw_triangle(length):
    for count in range(3):
        z.move_forward(length)
        z.turn_right(120)

def draw_house(length):
    draw_square(length)
    z.move_forward(length)
    z.turn_right(30)
    draw_triangle(length)
    # ???

# ???

z.check()
