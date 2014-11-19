import sys
sys.path.append('..')

import codestudio
artist = codestudio.load('enchcode4')

artist.color= 'random'

#TODO Redo the top to finish it
#It was supposed to draw a house
artist.turn_right(30)
for count2 in range(3):
    artist.move_forward(100)
    artist.turn_right(120)

artist.check()
