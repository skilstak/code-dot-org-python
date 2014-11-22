import sys
sys.path.append('../..')
import codestudio
a = codestudio.load('s1level24')
a.speed = 'fast'
a.move(100)
a.right()
#a.move(100)

a.check()

