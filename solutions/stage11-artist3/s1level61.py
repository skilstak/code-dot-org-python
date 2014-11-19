import sys
sys.path.append('../..')
import codestudio
z = codestudio.load('s1level61')

def draw_square(length):
    for count in range(4):
        z.move_forward(length)
        z.turn_right(90)

for count in range(3):
    z.color = z.random_color()
    draw_square(100)
    z.turn(120)

z.check()
