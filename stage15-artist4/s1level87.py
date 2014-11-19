"""Stage 15: Puzzle 6 of 10

Using `draw_square()` as an example, add an input named "length" to
`draw_triangle()`. Then, draw triangles in different sizes. 

"""

import sys
sys.path.append('..')
import codestudio
z = codestudio.load('s1level87')

def draw_square(length):
    for count in range(4):
        z.move_forward(length)
        z.turn_right(90)

def draw_triangle():
    for count in range(3):
        z.move_forward(100)
        z.turn_right(120)

# ???

z.check()
