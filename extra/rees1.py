import sys
sys.path.append('..')

import codestudio
artist = codestudio.load('rees1')

# TODO find and fix the bug

for count in range(4):
    for count in range(4):
        artist.color = 'random'
        artist.move_forward(20)
        artist.turn_right(90)
    artist.turn_left(90)
    artist.move_forward(20)

artist.check()

