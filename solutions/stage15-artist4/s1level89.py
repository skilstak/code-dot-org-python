import sys
sys.path.append('../..')
import codestudio
z = codestudio.load('s1level89')

def draw_square(length):
    for count in range(4):
        z.move_forward(length)
        z.turn_right(90)

def draw_triangle(length):
    for count in range(3):
        z.move_forward(length)
        z.turn_right(120)

def draw_house(length):
    draw_square(length)
    z.move_forward(length)
    z.turn_right(30)
    draw_triangle(length)
    z.right(60)
    z.move(length)
    z.right()
    z.move(length)
    z.flip()

draw_house(100)
draw_house(150)
draw_house(100)

z.check()
