import sys
sys.path.append('../..')
import codestudio
a = codestudio.load('s1level27')

for count in range(3):
    a.color = a.random_color()
    a.move(100)
    a.turn(120)
    
a.check()
