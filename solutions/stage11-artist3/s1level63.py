import sys
sys.path.append('../..')
import codestudio
z = codestudio.load('s1level63')
z.speed = 'fast'

def draw_square(length):
    for count in range(4):
        z.move_forward(length)
        z.turn_right(90)

draw_square(50)
draw_square(60)
draw_square(70)
draw_square(80)
draw_square(90)

z.check()
