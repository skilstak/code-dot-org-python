*Introduction to Computer Science*<br>Code.org in Python
========================================================

***This project has since been superceded by our use of [CodeCombat.com](http://codecombat.com) and our own [Python-0](http://github.com/skilstak/python-0) and [Python-1](http://github.com/skilstak.com/python-1) offerings
which teach real, typed Python the way college students and professions use it, from the Linux Bash command line. (Python IDLE sees far less actual use in the real world.)***


This repo contains the puzzles from the [Introduction to Computer Science
on code.org](http://learn.code.org/s/1) written in Python3 suitable for
any learning environment requiring only vanilla Python3 to be installed.
This includes the default Raspberry Pi setup. It was created to supplement
or replace the Blockly activities for those ready to ***actually*** write
 code. [Students 'create' code with Blockly they don't really 'write'
it.]

Students [fork this
repo](http://github.com/skilstak/code-dot-org-python/fork)
or [download the
zip](http://github.com/skilstak/code-dot-org-python/archive/master.zip)
and complete the puzzles with a vanilla installation of Python on
their local computer. Student code solutions are checked when they
run their code against a saved solution (in JSON format stored in a
[puzzles](/stage05-artist1/puzzles) directory). Detailed descriptions
from code.org for each puzzle are included as long comments at the beginning
of each puzzle script. If students get stuck they can refer to the
[solutions](/solutions). Teachers can easily create additional puzzles
for which the solutions are not available for more formal assessments
if needed.

As students progress in their porting to more complicated puzzles that
require use and creation of functions they put them into their own
version of the [mymod.py](mymod.py) module file.

Finally students can create their own puzzles for themselves
and others by contributing to the [extra collection](/extra), which may
eventually become its own site to students to puzzles each other.

The [codestudio](/codestudio) library module on which these puzzles
are based contains tools to help create new puzzles easily as well as
visualize puzzles and solutions. The steps to create your own puzzles
are outlined in [extras](/extra) with examples. The module itself
has been designed to serve as a basis for learning Python modules,
object-oriented-programming, packaging, geometry/trigonometry functions,
domain modeling, separation of concerns, exception handling, test-driven
development, basic GUI development, cross-platform audio programming,
JSON and more.

All code and assets are released under the same terms as the
[code-dot-org](http://github.com/code-dot-org) materials. We have
collaborated closely with the project team there.
