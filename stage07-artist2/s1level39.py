"""Stage 7: Puzzle 5 of 11

Here's the same code from the previous puzzle, but repeating the turns
36 times. How many degrees should the turns be? (Hint: after 360 degrees
of turning the drawing will come full circle)

"""

import sys
sys.path.append('..')
import codestudio
artist = codestudio.load('s1level39')
artist.speed = 'faster'
a = artist

for count2 in range(36):
    artist.color = artist.random_color()
    for count in range(3):
        artist.move_forward(100)
        artist.turn_right(120)
    artist.turn_right(2)                         # ???

artist.check()
