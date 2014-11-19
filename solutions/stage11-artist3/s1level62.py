import sys
sys.path.append('../..')
import codestudio
z = codestudio.load('s1level62')
z.speed = 'faster'

def draw_square(length):
    for count in range(4):
        z.move_forward(length)
        z.turn_right(90)

for count in range(36):
    z.color = z.random_color()
    draw_square(100)
    z.turn_right(10)

z.check()
