Make Your Own Puzzles!
=========================

Here are some extra puzzles created by students young and old. Some are
very easy, some very hard. See if you can do them. Then, create your own
puzzles to submit and we'll include them as well. Here's how ...

1. Copy the `sample.py` or another than you like.
2. Change `load(whatever)` to `create(uid,type,start_direction,startx,starty,title)` 
3. Change `check()` to `wait()` until you perfect your puzzle
4. Change `wait()` to `save()` when you are ready to save it. Then run again.
5. Change the `create()` to `load(uid)`
6. Change the `save()` to `check()`
7. Test run it again with your solution
8. Remove or change the lines of code you want players to fix or add
9. Run one last time to test what your players will see
10. Commit your changes to github and let us know about them to include

`start_direction`, `startx`, `starty` and `title` are optional. That's
it. Here's an example:

```
"""Draw a Square

Draw a square in three lines of code.
"""

import sys
sys.path.append('..')
import codestudio
artist = codestudio.create('square-loop','artist',90,0,0,'Draw a Square')

for count in range(4):
    artist.move_forward(100)
    artist.turn_right(90)

artist.save()
```

This will automatically save it into the `puzzles` directory for you
and make sure there isn't one already saved there with your unique id.

The parameters to `create()` are to help identify the puzzle solution and
setup the starting settings:

1. A required string that will be the unique name and file name
2. A required type of code.org puzzle ('artist', 'maze', or 'farmer')
3. An optional starting direction to face (default 0, which is up)
4. An optional starting x coordinate offset (default 0)
5. An optional starting y coordinate offset (default 0) 
6. An optional title (default 'codestudio')

All you need to do after that is test your challenge by changing
`create()` and `save()` to `load()` and `check()`:

```
"""Draw a Square

Draw a square in three lines of code.
"""

import sys
sys.path.append('..')
import codestudio
artist = codestudio.load('square-loop')

for count in range(4):
    artist.move_forward(100)
    artist.turn_right(90)

artist.check()
```

Now just remove the code you want coders to figure out and replace with
some comments to give them hints, but they will already get the solution
drawn for them to see. *Make sure your code contains nothing left off,
like loops without a body, because it will stop the solution from even
appearing. Use `pass` if you need to for empty loops and such.*

Place hint `# ???` comments either on the line where they should begin
or on column 50 of the same line if that line needs to be changed.

```
"""Draw a Square

Draw a square in three lines of code.
"""

import sys
sys.path.append('..')
import codestudio
artist = codestudio.load('square-loop')

for count in range(4):
    pass                                         # ???

artist.check()
```

Keep in mind that if you want to change your saved puzzle later you will
have to edit the `json` file directly in the `puzzles` folder that you
saved for it or remove it and create the puzzle again. `artist.save()` will
never overwrite an existing saved solution to keep you from breaking
others that are already working.

Gotchas for Developers
======================

# Don't forget `sys.path.append('..')`

Don't forget to add the following two lines so that folks can just
solve these extras without moving anything or setting their
`PYTHONPATH`, which they might not have learned how to do yet:

```
import sys
sys.path.append('..')
import codestudio
```

This also allows others to create their own collection of code puzzle
challenges just by creating a directory structure or github repo like this:

```
./puzzles/sample.py
./sample.py
./README.md
```

# You don't need `__author__` and `__credits__`

People can see who contributed what by looking where they should, at
the source files on GitHub. Adding these tags just makes more work
to maintain them. Add a README.md file instead.

# Make sure challenge fits on 400 pixel square canvas

This is small, sure, but it allows your challenges to match those from
code.org and fit next to a coding window open on the right. It also allows
for future `codestudio` Python development to add other widgets to the
main window.
