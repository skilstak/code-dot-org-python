"""Stage 7: Puzzle 11 of 11

Try changing the numbers in the turn function calls and repeat (for) loops
to make different patterns. Or, experiment changing the rest of the code
to draw anything you want.

"""

import sys
sys.path.append('..')
import codestudio
artist = codestudio.load('s1level45')
artist.speed = 'fastest'

for count3 in range(18):
    for count2 in range(10):
        artist.color = artist.color_random()
        for count in range(4):
            artist.move_forward(20)
            artist.turn_right(90)
        artist.move_forward(20)
    artist.turn_right(100)

artist.wait()
