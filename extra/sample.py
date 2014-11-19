import sys
sys.path.append('..')
import codestudio
artist = codestudio.load('sample')

artist.color= 'random'

for counter in range(4):
    # TODO draw one side and turn
    pass

artist.check()
