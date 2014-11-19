"""Stage 15: Puzzle 1 of 10

This puzzle shows you how the `draw_square()` and `draw_circle()`
functions are defined. Defining a function doesn't run its blocks. You
have to call `draw_square()` function to actually draw a square. Note:
in this Python version of code.org you have seen these functions all
along in the Stage 11 puzzle code but we focus on them now to explain
how to define them.

"""
import sys
sys.path.append('../..')
import codestudio
z = codestudio.load('s1level82')

def draw_square():
    for count in range(4):
        z.move_forward(100)
        z.turn_right(90)

def draw_circle():
    saved_speed = z.speed
    z.speed = 'fastest'
    for count in range(360):
        z.move_forward(1)
        z.turn_right(1)
    z.speed = saved_speed

draw_square()

z.check()
