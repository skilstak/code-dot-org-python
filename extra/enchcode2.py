import sys
sys.path.append('..')

import codestudio
artist = codestudio.load('enchcode2')

artist.color= 'random'
artist.speed= 'fastest'

for counter in range(4):
    #TODO Draw a square with sides of 100
    pass
artist.check()
