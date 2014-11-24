"""Stage 11: Puzzle 9 of 11

This one's a bit tricky. Use the `draw_snowman()` function and the new
`jump_forward(100)` or just `jump(100)`. Draw 3 snowmen in different
colors, 100 pixels apart.

"""

import sys
sys.path.append('..')
import codestudio
zombie = codestudio.load('s1level67')
z = zombie

def draw_snowman(length):
    zombie.left()
    distances = [length * 0.5, length * 0.3, length * 0.2]
    for counter in range(6):
        distance = distances[counter if counter < 3 else 5 - counter] / 57.5
        for degree in range(90):
            zombie.move(distance)
            zombie.right(2)
        if counter != 2:
            zombie.left(180)
    zombie.left()

zombie.speed = 'fastest'

draw_snowman(150)

zombie.check()
