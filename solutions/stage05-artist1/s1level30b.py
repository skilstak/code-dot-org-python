import sys
sys.path.append('../..')
import codestudio
a = codestudio.load('s1level30')

a.right()
for count in range(4):
    a.move(100)
    a.right()
a.flip()
a.move(50)
for count in range(4):
    a.move(100)
    a.left()

a.check()
