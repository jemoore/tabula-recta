#!/usr/bin/env python

from random import randint
from random import seed
from string import ascii_uppercase

seed(73)

for r in range(27):
    if r == 0:
        print "  ", 
        for s in ascii_uppercase:
            print s,# " ",
        print
        print '-' * 55
        continue
    for c in range(27):
        if c == 0:
            print ascii_uppercase[r-1] + '|', #" ",
        else:
            print chr(randint(33,126)), #" ",
    print

