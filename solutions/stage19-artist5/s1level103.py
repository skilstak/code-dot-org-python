import sys
sys.path.append('../..')
import codestudio
z = codestudio.load('s1level103')

for counter in range(1,201,1):
    z.color = z.random_color()
    z.move_forward(counter)
    z.turn_right(90)

z.wait()
