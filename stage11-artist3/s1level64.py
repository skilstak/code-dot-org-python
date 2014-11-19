"""Stage 11: Puzzle 6 of 11

Ok, this program will use a counter to draw the same squares as last time
(50,60,70,80,90). You want the square to be the same size as the counter,
so use the "counter" loop. Here's how:

Counter loops are the same as the simple `for counter in range(4):` loops
just with extra `range()` parameters and we actually use the `counter`
variable that gets set every time through the loop. It doesn't have to
be named `counter` but we use that name for consistency in these puzzles.

    for counter in range(5,51,5):
        print(counter)

The first number (5) is the one to start with.

The second number (51) is the maximum plus 1. We add a 1 so that 50 will
be included.

The third (5) is how much to count by (5,10,15,...50).

Even though we have to add 1 to count the way we want, note how much
cleaner Python loops are than the ones used in JavaScript (from 'Show
Code') and other languages.

"""

import sys
sys.path.append('..')
import codestudio
zombie = codestudio.load('s1level64')

def draw_square(length):
    for count in range(4):
        zombie.move_forward(length)
        zombie.turn_right(90)

zombie.speed = 'fast'

smallest = 10                                    # ???
longest = 60                                     # ???
by = 20                                          # ??? 

for counter in range(smallest, longest + 1, by):
    draw_square(counter)

zombie.check()
