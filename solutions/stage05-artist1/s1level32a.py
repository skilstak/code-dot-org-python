import sys
sys.path.append('../..')
import codestudio
a = codestudio.load('s1level32')
a.speed = 'fastest'

for count in range(360):
    a.move_forward(1)
    a.turn_right(1)

a.check()
