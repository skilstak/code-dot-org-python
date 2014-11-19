"""Stage 19: Puzzle 2 of 6

Try running this program, and make changes to see what happens. Can you
figure out how it works? (Or delete it and replace it with something
totally different)

"""

import sys
sys.path.append('..')
import codestudio
z = codestudio.load('s1level104')

for counter in range(1,300,1):
    z.color = z.random_color()
    z.move_forward(counter)
    z.turn_right(121)

z.wait()
