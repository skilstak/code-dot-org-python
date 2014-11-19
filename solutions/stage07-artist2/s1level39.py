import sys
sys.path.append('../..')
import codestudio
a = codestudio.load('s1level39')
a.speed = 'faster'

for count2 in range(36):
    a.color = a.random_color()
    for count in range(3):
        a.move_forward(100)
        a.turn_right(120)
    a.turn_right(10)

a.check()
