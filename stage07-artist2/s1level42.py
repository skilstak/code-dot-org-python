"""Stage 7: Puzzle 8 of 11

Here's the solution to the previous puzzle. Can you add just 2 more
lines of code to complete the drawing?

"""

import sys
sys.path.append('..')
import codestudio
artist = codestudio.load('s1level42')
artist.speed = 'faster'
a = artist

for count2 in range(10):
    artist.color = artist.random_color()
    for count in range(4):
        artist.move_forward(20)
        artist.turn_right(90)
    artist.move_forward(20)

artist.check()
