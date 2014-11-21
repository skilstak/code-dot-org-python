"""Stage 7: Puzzle 2 of 11

Add "turn right by 90 degrees" code somewhere in the middle of the
program already written below to draw these triangles.

"""

import sys
sys.path.append('../..')
import codestudio
a = codestudio.load('s1level36')

a.color = a.random_color()
for count in range(3):
    a.move_forward(100)
    a.turn_right(120)
a.color = a.random_color()
a.right()
for count in range(3):
    a.move_forward(100)
    a.turn_right(120)

a.check()
