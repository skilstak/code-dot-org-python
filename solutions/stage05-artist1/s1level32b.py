import sys
sys.path.append('../..')
import codestudio
a = codestudio.load('s1level32')
a.speed = 'fastest'

for count in range(360):
    a.move_backward(1)
    a.left(1)

a.check()
