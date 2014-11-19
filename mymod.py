"""Example module to contain methods, functions and variables for reuse.

This file gets loaded as a module (sometimes also called a library) when
you call `import mymod` in your scripts.

"""

import codestudio

class Zombie(codestudio.Artist):
    """An Artist with a propensity for brains and drawing squares.

    While class definitions look like function definitions they are different.
    The parameter inside the parenthesis () is the parent class. This means
    all Zombies are Artists and can do everything an Artist can do.

    The `start_direction` and `speed` are special variables that goes with
    all Zombies. These are called class or static attributes. An attribute
    is a variable that goes with a class or the objects created from a class.
    """
    start_direction = 90            # facing the east, or right of screen
    speed = 'slow'                  # it is a zombie after all
    color = 'green'                 # it is a zombie after all

    def draw_square(self,length):
        for count in range(4):
            self.move_forward(length)
            self.turn_right(90)

    def draw_circle(self):
        saved_speed = zombie.speed
        zombie.speed = 'fastest'
        for count in range(360):
            zombie.move_forward(1)
            zombie.turn_right(1)
        zombie.speed = saved_speed

    def draw_snowman(self,length):
        self.left()
        distances = [length * 0.5, length * 0.3, length * 0.2]
        for counter in range(6):
            distance = distances[counter if counter < 3 else 5 - counter] / 57.5
            for degree in range(90):
                self.move(distance)
                self.right(2)
            if counter != 2:
                self.left(180)
        self.left()
