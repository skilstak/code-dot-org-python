import sys
sys.path.append('../..')
import codestudio
z = codestudio.load('s1level59')

for count in range(4):
    z.move(100)
    z.right()

z.check()
