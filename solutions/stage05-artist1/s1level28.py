import sys
sys.path.append('../..')
import codestudio
a = codestudio.load('s1level28')

for count in range(3):
    a.move(100)
    a.turn(120)
for count in range(4):
    a.move(100)
    a.turn(90)

a.check()
