import sys
import math

# game loop
'''
mh = []

while True:
    for i in range(8):
        mh.append(int(input()))  # represents the height of one mountain.
        m = max(mh)
        i = mh.index(m)
    print(i)
    mh = []
'''

while True:
    heights = [int(input()) for i in range(8)]
    print(heights.index(max(heights)))
