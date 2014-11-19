"""Stage 5: Puzzle 9 of 10

Can you figure out what number to replace the 25 with to
draw a circle?

"""

import sys
sys.path.append('..')
import codestudio
artist = codestudio.load('s1level32')
artist.speed = 'fastest'

for count in range(25):                          # ???
    artist.move_forward(1)
    artist.turn_right(1)

artist.check()
