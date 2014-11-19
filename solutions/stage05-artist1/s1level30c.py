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
a.left()
for count in range(4):
    a.move(100)
    a.right()

a.check()
