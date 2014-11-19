"""Stage 7: Puzzle 4 of 11

Here's the same code from the previous puzzle, but turning only 36
degrees after drawing each triangle. How many times does this need
to repeat? (Hint: after 360 degrees of turning the drawing will come
full circle)

"""

import sys
sys.path.append('..')
import codestudio
artist = codestudio.load('s1level38')

for count2 in range(2):
    artist.color = artist.colour_random()
    for count in range(3):
        artist.move_forward(100)
        artist.turn_right(120)
    artist.turn_right(36)

artist.check()
