import sys
sys.path.append('../..')
import codestudio
a = codestudio.load('s1level24')
a.speed = 'slowest'

a.move(100)
a.right()
a.move(100)

a.check()

