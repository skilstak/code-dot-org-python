import sys
sys.path.append('../..')
import codestudio
a = codestudio.load('s1level37')

a.color = a.color_random()
for count in range(4):
    for count in range(3):
        a.move_forward(100)
        a.turn_right(120)
    a.right()

a.check()
