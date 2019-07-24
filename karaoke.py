import re
import os
import glob

title_artist = re.compile(r'[\w ]+–[\w ]+')
title_artist_notes = re.compile(r'[\w ]+–[\w ]+(\([\w ]+\))$')

path = './lists'

for filename in glob.glob(os.path.join(path, '*.txt')):
    with open(filename, 'r') as f:
        content = f.readlines()
    content = [x.strip() for x in content] 
    
    line_number = 0
    print(filename)
    for line in content:
        line_number += 1
        print('%d %s' % (line_number, line))