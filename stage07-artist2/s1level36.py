"""Stage 7: Puzzle 2 of 11

Add "turn right by 90 degrees" code somewhere in the middle of the
program already written below to draw these triangles.

"""

import sys
sys.path.append('..')
import codestudio
artist = codestudio.load('s1level36')
a = artist

artist.color = artist.random_color()
for count in range(3):
    artist.move_forward(100)
    artist.turn_right(120)
artist.color = artist.random_color()
for count in range(3):
    artist.move_forward(100)
    artist.turn_right(120)

artist.check()
