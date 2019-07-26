#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import os
import glob
import datetime

VENUE = re.compile(r'\d{4}\-\d{2}\-\d{2} –[\w \-\']+')
VENUE_NOTES = re.compile(r'\d{4}\-\d{2}\-\d{2} –[\w \-\']+(\([\w \-\',]+\))$')
TITLE_ARTIST = re.compile(r'[\w \-\']+–[\w \-\']+')
TITLE_ARTIST_NOTES = re.compile(r'[\w \-\']+–[\w \-\']+(\([\w \-\',]+\))$')

PATH = './lists'

class Song:
    title = ''
    artist = ''

    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

class Venue:
    name = ''

    def __init__(self, name):
        self.name = name

class Night:
    venue = None
    date = None
    songs = []
    notes = ''

    def __init__(self, venue, date):
        self.venue = venue
        self.date = datetime.date(int(date[:4]), int(date[5:7]), int(date[8:]))

    def add_song(self, title='', artist='', song=None):
        if song is None:
            song = Song(title, artist)
        self.songs.append(song)

for filename in glob.glob(os.path.join(PATH, '*.txt')):
    with open(filename, 'r', encoding='utf8') as f:
        content = f.readlines()
    content = [x.strip() for x in content] 
    
    nights = []
    suggestions = []
    empty_flag = False
    suggestions_flag = False
    for line in content:
        if VENUE_NOTES.match(line):
            empty_flag = False
            notes_index = line.find('(') + 1

            date = line[:10]
            venue = line[13:notes_index - 2]
            notes = line[notes_index:-1]

            print('# %s – %s (%s)' % (date, venue, notes))
        elif VENUE.match(line):
            empty_flag = False

            date = line[:10]
            venue = line[13:]

            print('@ %s – %s' % (date, venue))
        elif TITLE_ARTIST_NOTES.match(line):
            if empty_flag == True:
                suggestions_flag = True:
            empty_flag = False

            separator_index = line.find(' – ')
            notes_index = line.find('(') + 1
            title = line[0:separator_index]
            artist = line[separator_index + 3:notes_index - 2]
            notes = line[notes_index:-1]

            print('+ %s – %s (%s)' % (title, artist, notes))
        elif TITLE_ARTIST.match(line):
            if empty_flag == True:
                suggestions_flag = True:
            empty_flag = False

            separator_index = line.find(' – ')
            title = line[0:separator_index]
            artist = line[separator_index + 3:]

            print('- %s – %s' % (title, artist))
        elif line == '':
            empty_flag = True
            suggestions_flag = False:
            print('')
        else:
            print('  %s' % line)

    print('')