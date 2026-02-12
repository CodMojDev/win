import random
import shutil
import os

win = os.path.dirname(os.path.dirname(__file__))

if os.path.exists('public-win'):
    shutil.rmtree('public-win')
    
shutil.copytree(win, 'public-win', ignore=lambda p, q: ('public-win'))

for dirpath, dirnames, filenames in os.walk('public-win'):
    if '__pycache__' in dirnames:
        shutil.rmtree(os.path.join(dirpath, '__pycache__'))
            
open('public-win/com/data/guids.dat', 'wb').close() # clear GUIDS cache
os.remove('public-win/tools/publish.py') # only DEV