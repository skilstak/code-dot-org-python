import sys
sys.path.append('../..')
import codestudio
a = codestudio.load('s1level33')

a.color = a.random_color()
a.width = 1
a.move_forward(100)

a.wait()
