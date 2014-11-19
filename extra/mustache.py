import sys
sys.path.append('..')

import codestudio
artist = codestudio.load('mustache')
artist.width = 4
artist.speed = 'fastest'

# TODO make less Vegas

for counter in range(1,720):
    artist.color= 'random'
    artist.move(10)
    artist.right(10) # hummmmm
    
artist.check()
