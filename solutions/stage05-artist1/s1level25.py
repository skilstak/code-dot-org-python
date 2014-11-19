import sys
sys.path.append('../..')
import codestudio
a = codestudio.load('s1level25')

a.color = 'red'

for count in range(4):
    a.move(100)
    a.right()

a.check()
