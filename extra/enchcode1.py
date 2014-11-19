import sys
sys.path.append('..')

import codestudio
artist = codestudio.load('enchcode1')

artist.color= 'blue'
artist.speed= 'fastest'
artist.width= '5'

for counter in range(360):
    #TODO Draw a blue circle
    pass

artist.check()
