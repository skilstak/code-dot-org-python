import sys
sys.path.append('../..')
import codestudio
z = codestudio.load('s1level65')

for length in range(25,61,5):
    z.move_forward(length)
    z.right()

z.check()
