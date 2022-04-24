import sys
import math
import string

ascii = string.ascii_uppercase + string.ascii_lowercase
s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ?'
line = ''

l = int(input())
h = int(input())
t = input()

for i in range(h):
    row = input()
    for c in t:
        if set(c).issubset(ascii):
            block = row[s.index(c.upper())*l:s.index(c.upper())*l+l]
        else: 
            block = row[26*l:26*l+l]
        line += block
    print(line)
    line = ''