import sys
sys.path.append('../..')
import codestudio
z = codestudio.load('s1level107')

def draw_circle(step):
    saved_speed = z.speed
    z.speed = 'fastest'
    for count in range(60):
        z.move_forward(step)
        z.turn_right(6)
    z.speed = saved_speed

for counter in range(4,9,4):
    for count in range(10):
        z.color = z.random_color()
        draw_circle(counter)
        z.turn_right(36)

z.wait()
