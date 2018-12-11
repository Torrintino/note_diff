#!/usr/bin/python3

import random

notes = ['A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D',
         'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab']

a = random.randrange(12)
b = a
while a == b:
    b = random.randrange(12)
answer = int(input('How many steps do you need from {} to {}?\n'.format(
    notes[a], notes[b])), 10)
if (notes[b] == notes[(a + answer) % 12] or
    notes[b] == notes[(a - answer) % 12]):
    print('Correct.\n')
else:
    print('False.\n')
