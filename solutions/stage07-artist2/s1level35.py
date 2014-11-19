import sys
sys.path.append('../..')
import codestudio
a = codestudio.load('s1level35')

for count in range(3):
    a.move(100)
    a.turn(120)

a.check()
