import sys
sys.path.append('../..')
import codestudio
z = codestudio.load('s1level83')

def draw_square():
    for count in range(4):
        z.move_forward(100)
        z.turn_right(90)

def draw_triangle():
    for count in range(3):
        z.move(100)
        z.right(120)

draw_triangle()

z.check()
