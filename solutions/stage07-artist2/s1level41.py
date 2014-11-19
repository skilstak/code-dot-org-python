import sys
sys.path.append('../..')
import codestudio
a = codestudio.load('s1level41')

a.color = a.random_colour()
for count in range(10):
    for count in range(4):
        a.move_forward(20)
        a.turn_right(90)
    a.move(20)

a.check()
