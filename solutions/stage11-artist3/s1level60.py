import sys
sys.path.append('../..')
import codestudio
z = codestudio.load('s1level60')

def draw_square(length):
    for count in range(4):
        z.move_forward(length)
        z.turn_right(90)

draw_square(50)

z.check()
