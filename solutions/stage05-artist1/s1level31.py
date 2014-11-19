import sys
sys.path.append('../..')
import codestudio
a = codestudio.load('s1level31')

for count in range(8):
    a.color = a.random_color()
    a.move_forward(100)
    a.move_backward(100)
    a.turn_right(45)

a.check()
