import sys
sys.path.append('../..')
import codestudio
z = codestudio.load('s1level69')

def draw_square(length):
    for count in range(4):
        z.move_forward(length)
        z.turn_right(90)

def draw_snowman(length):
    z.left()
    distances = [length * 0.5, length * 0.3, length * 0.2]
    for counter in range(6):
        distance = distances[counter if counter < 3 else 5 - counter] / 57.5
        for degree in range(90):
            z.move(distance)
            z.right(2)
        if counter != 2:
            z.left(180)
    z.left()

z.speed = 'fast'
z.width = 1

for counter in range(100):
    z.move(counter)
    z.right(91)

z.wait()
