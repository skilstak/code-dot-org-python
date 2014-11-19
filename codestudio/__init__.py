r"""The `codestudio` module contains all the <http://studio.code.org>
challenges and code to complete, extend, and add to them. Each challenge
is created in JSON and stored in `challenges`. Students complete the
challenges by completing the missing portions of the stub `py` files for
each challenge and then running them until they succeed. Challenges can
also be created using the `challenge.save(fname)` method. Successful
completions can optionally be reported to any accessible web site
supporting the `codestudio.progress` web API.

The only dependency is that standard Python 3 be installed from
<http://python.org>. This absence of other dependencies is by design to
best enable students, teachers, and developers to get up and running as
quickly as possible. This module requires only Python 3 with `tkinter`
and the standard sound libraries for each operating system from Multimedia
Services as described on <https://docs.python.org/3/library/mm.html>.

The implementation in `tkinter` has been abstracted away sufficient to be
replaced by other graphics libaries. This also allows the model itself to
be used to teach object-oriented programming without the distraction of
the graphics package implementation, which can later be taught through
its use as a graphics engine for this project. It also allows the base
`codestudio` domain and object model to be easily ported between different
object-oriented languages.

"""

import json
from os import path
from .artist import Artist
#from .maze import MazePlayer
#from .farmer import Farmer

def load(uid):
    fname = uid + '.json'
    local = path.join('.',fname)
    pname = path.join('puzzles',fname)
    if path.isfile(local):
        pname = local
    assert path.isfile(pname), 'Puzzle not found for {}.'.format(uid) 
    with open(pname, 'r') as f:
        config = json.load(f)
        if not 'uid' in config.keys(): config['uid'] = uid
        ctype = config['type']
        if ctype == 'artist':
            player = Artist.from_json(config)
        #elif ctype == 'maze':
        #    player = MazePlayer.from_json(config)
        #elif ctype == 'farmer':
        #    player = Farmer.from_json(config)
        else:
            raise Exception('Invalid or missing puzzle type')
    player.setup()
    return player

def create(uid,ctype,direction=0,x=0,y=0,title=None):
    '''Combine with `save()` to create new puzzles'''
    fname = path.join('puzzles',uid+'.json')
    assert not path.isfile(fname), '{} already exists'.format(fname)
    config = {
        'uid': uid,
        'start_direction': direction,
        'startx': x,
        'starty': y,
        'title': title
    }
    if ctype == 'artist':
        player = Artist.from_json(config)
    #elif ctype == 'maze':
    #    player = MazePlayer.from_json(config)
    #elif ctype == 'farmer':
    #    player = Farmer.from_json(config)
    player.setup()
    return player
