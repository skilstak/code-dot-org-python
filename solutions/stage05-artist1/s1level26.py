import sys
sys.path.append('../..')
import codestudio
a = codestudio.load('s1level26')

for count in range(4):
    a.move(100)
    a.right()

a.check()
