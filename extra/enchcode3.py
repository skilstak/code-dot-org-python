import sys
sys.path.append('..')

import codestudio
artist = codestudio.load('enchcode3')

artist.color= 'red'

for count in range(4):
    artist.move_forward(100)
    artist.turn_right(90)
#TODO Replace this with a line to make
#2 squares next to each other
for count2 in range(4):
    artist.move_forward(100)
    artist.turn_right(90)

artist.check()
