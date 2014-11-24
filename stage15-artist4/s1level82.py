"""Stage 15: Puzzle 1 of 10

This puzzle shows you how the `draw_square()` and `draw_circle()`
functions are defined. Defining a function doesn't run its blocks. You
have to call `draw_square()` function to actually draw a square. Note:
in this Python version of code.org you have seen these functions all
along in the Stage 11 puzzle code but we focus on them now to explain
how to define them.

"""
import sys
sys.path.append('..')
import codestudio
zombie = codestudio.load('s1level82')
z = zombie

def draw_square():
    for count in range(4):
        zombie.move_forward(100)
        zombie.turn_right(90)

def draw_circle():
    saved_speed = zombie.speed
    zombie.speed = 'fastest'
    for count in range(360):
        zombie.move_forward(1)
        zombie.turn_right(1)
    zombie.speed = saved_speed

# ???

zombie.check()
