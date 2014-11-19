import sys
sys.path.append('../..')
import codestudio
a = codestudio.load('s1level38')

for count2 in range(10):
    a.color = a.colour_random()
    for count in range(3):
        a.move_forward(100)
        a.turn_right(120)
    a.turn_right(36)

a.check()
