import sys
sys.path.append('../..')
import codestudio
z = codestudio.load('s1level68')

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

z.speed = 'fastest'

for length in range(110,69,-10):
    draw_snowman(length)
    z.right()
    z.jump(60)
    z.left()

z.check()
