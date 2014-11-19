import sys
sys.path.append('../..')
import codestudio
a = codestudio.load('s1level40')
a.speed = 'slow'

for count in range(4):
    a.move(20)
    a.right()

a.check()
