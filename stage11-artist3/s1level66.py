"""Stage 11: Puzzle 8 of 11

There's a new `draw_snowman()` function. Draw two snowmen, of height
250 and 100.

"""

import sys
sys.path.append('..')
import codestudio
zombie = codestudio.load('s1level66')

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

draw_snowman(250)
# ???

zombie.check()
