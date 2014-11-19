"""Stage 7: Puzzle 9 of 11

Here's the solution to the previous puzzle. How many degrees should you
turn to complete the drawing? (You probably need to guess a few times.)

"""

import sys
sys.path.append('..')
import codestudio
artist = codestudio.load('s1level43')
artist.speed = 'fastest'

for count3 in range(4):
    for count2 in range(10):
        artist.color = artist.color_random()
        for count in range(4):
            artist.move_forward(20)
            artist.turn_right(90)
        artist.move_forward(20)
    artist.turn_right(45)                        # ???

artist.check()
