import sys
sys.path.append('../..')
import codestudio
a = codestudio.load('s1level29')

for count in range(3):
    a.move(100)
    a.turn(120)
a.turn(180)
for count in range(4):
    a.move(100)
    a.right()
    
a.check()
