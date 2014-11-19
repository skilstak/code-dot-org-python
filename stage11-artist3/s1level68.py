"""Stage 11: Puzzle 10 of 11

Now for a real challenge. Use a counter (for) loop to draw a family of
snowmen with heights of 110, 100, 90, 80, and 70. The snowmen should
all be 60 pixels apart.  Hint: Remember you are counting backwards (use
-). Also use 69 instead of 70 to make sure you get enough snowmen. Hint:
read Puzzle 6 (s1level64) if you need to remember how to do counter
loops in Python.

"""

import sys
sys.path.append('..')
import codestudio
zombie = codestudio.load('s1level68')

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

for length in range(0):                          # ???
    draw_snowman(length)
    # ???

zombie.check()
