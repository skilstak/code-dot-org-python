import sys
sys.path.append('../..')
import codestudio
a = codestudio.load('s1level44')
a.speed = 'fastest'

for count3 in range(10):
    for count2 in range(10):
        a.color = a.random_colour()
        for count in range(4):
            a.move_forward(20)
            a.turn_right(90)
        a.move_forward(20)
    a.turn_right(80)

a.check()
