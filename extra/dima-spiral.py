import sys
sys.path.append('..')
import codestudio
artist = codestudio.load('dima-spiral')
artist.speed = 'fastest'

artist.width = 5
artist.color = 'random'

for counter in range(1,501,5):
    artist.move_forward(counter)
    artist.turn_right(91)

artist.wait()
