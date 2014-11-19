"""Stage 7: Puzzle 10 of 11

Here's a change to the previous puzzle. How many times should you
repeat to complete the drawing?

"""

import sys
sys.path.append('..')
import codestudio
artist = codestudio.load('s1level44')
artist.speed = 'fastest'

for count3 in range(1):                          # ???
    for count2 in range(10):
        artist.color = artist.random_colour()
        for count in range(4):
            artist.move_forward(20)
            artist.turn_right(90)
        artist.move_forward(20)
    artist.turn_right(80)

artist.check()
