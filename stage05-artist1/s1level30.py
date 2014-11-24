"""Stage 5: Puzzle 7 of 10

Ok, let's make it a bit harder - see if you can draw these green
glasses. The squares are 100 pixels on each side, and they're 50 pixels
apart. Don't forget to draw in green! 

"""

import sys
sys.path.append('..')
import codestudio
artist = codestudio.load('s1level30')
a = artist

artist.color = 'green'
artist.right(90)
# ???

artist.check()
