import sys
sys.path.append('../..')
import codestudio
a = codestudio.load('s1level30')

a.right()
for count in range(4):
    a.move(100)
    a.right()
a.flip()
a.move(150)
for count in range(3):
    a.left()
    a.move(100)

a.check()
