"""Stage 11: Puzzle 4 of 11

Now we're going to get fancy. Change the code to draw 36 squares, 100
pixels wide, and each 10 degrees apart. Hint: adjust the speed by setting
to 'normal', 'fast', 'faster', 'fastest' or a number.

"""

import sys
sys.path.append('..')
import codestudio
zombie = codestudio.load('s1level62')
zombie.speed = 'faster'
z = zombie

def draw_square(length):
    for count in range(4):
        zombie.move_forward(length)
        zombie.turn_right(90)

for count in range(10):                          # ???
    zombie.color = zombie.random_color()
    draw_square(50)                              # ???
    zombie.turn_right(20)                        # ???

zombie.check()
