import sys
sys.path.append('../..')
import codestudio
z = codestudio.load('s1level64')

def draw_square(length):
    for count in range(4):
        z.move_forward(length)
        z.turn_right(90)

z.speed = 'fast'

smallest = 50
longest = 90
by = 10

for counter in range(smallest, longest + 1, by):
    draw_square(counter)

z.check()
