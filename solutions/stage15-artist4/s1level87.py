import sys
sys.path.append('../..')
import codestudio
z = codestudio.load('s1level87')

def draw_square(length):
    for count in range(4):
        z.move_forward(length)
        z.turn_right(90)

def draw_triangle(length):
    for count in range(3):
        z.move_forward(length)
        z.turn_right(120)

draw_triangle(100)
z.move(100)
draw_triangle(200)

z.check()
