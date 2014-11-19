"""Stage 15: Puzzle 7 of 10

Add an input named "length" to `draw_house()` and build a big house for
the elephant (with edges 150 pixels long)

"""

import sys
sys.path.append('..')
import codestudio
z = codestudio.load('s1level88')

def draw_square(length):
    for count in range(4):
        z.move_forward(length)
        z.turn_right(90)

def draw_triangle(length):
    for count in range(3):
        z.move_forward(length)
        z.turn_right(120)

def draw_house():
    draw_square(100)
    z.move_forward(100)
    z.turn_right(30)
    draw_triangle(100)

# ???

z.check()
