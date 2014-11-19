import sys
sys.path.append('../..')
import codestudio
z = codestudio.load('s1level108')
z.speed = 'faster'

def draw_tree(depth,branches):
    if depth > 0:
        z.color = z.random_color()
        z.move_forward(7*depth)
        z.turn_left(130)
        for count in range(branches):
            z.turn_right(180/branches)
            draw_tree(depth-1,branches)
        z.turn_left(50)
        z.jump_backward(7*depth)

draw_tree(9,2)

z.wait()
