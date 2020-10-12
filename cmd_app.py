#pip install doc
from docopt import docopt
import test_app 



usage ='''
usage:

cmd_app.py  --init

'''

args= docopt(usage)


if args['--init']:
    print('hello')
