"""Stage 7: Puzzle 3 of 11

Ok, here's the code you wrote to draw a single triangle. Can you add a
repeat (for) loop and turn function call to make a pretty flower?

"""

import sys
sys.path.append('..')
import codestudio
artist = codestudio.load('s1level37')
artist.speed = 'slow'

artist.color = artist.color_random()
for count in range(3):
    artist.move_forward(100)
    artist.turn_right(120)

artist.check()
