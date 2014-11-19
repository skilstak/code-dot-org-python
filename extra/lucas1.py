import sys
sys.path.append('..')

import codestudio
artist = codestudio.load('lucas1')

artist.color = 'random'
artist.width = 2
artist.speed = 'faster'

# TODO make it, if you can, lol
# ok, one hint, the loop draws 250 lines
# but has a maximum counter value of 500

#for counter in range(??,500,??)

artist.check()
