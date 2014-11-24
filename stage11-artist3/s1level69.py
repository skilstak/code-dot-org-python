"""Stage 11: Puzzle 11 of 11

Here's some code to try experimenting with different spirals. What happens
if you change the turn amount? Or set a random color in the loop? Draw
anything you like.

"""

import sys
sys.path.append('..')
import codestudio
zombie = codestudio.load('s1level69')
z = zombie

def draw_square(length):
    for count in range(4):
        zombie.move_forward(length)
        zombie.turn_right(90)

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

zombie.speed = 'fast'
zombie.width = 1

for counter in range(100):
    zombie.move(counter)
    zombie.right(91)

zombie.wait()
